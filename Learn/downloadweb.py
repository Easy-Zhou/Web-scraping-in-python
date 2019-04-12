#!/anaconda3/bin/python
# @Time    : 2019-04-10 13:04
# @Author  : zhou
# @File    : downloadweb
# @Software: PyCharm
# @Description:
import itertools
import re
import urllib.request
from urllib import robotparser
from urllib.error import URLError, HTTPError, ContentTooShortError
from urllib.parse import urljoin


def download(url, user_agent='wswp', num_retries=2, charset='utf-8'):
    """
    下载网页
    :param url: 网页地址 如：https://www.baidu.com
    :param user_agent: 用户代理 default wswp
    :param num_retries: 重试下载次数 default 2
    :param charset: 网页编码方式 default utf-8
    :return: 抓取的网页html
    """
    print('Downloading:', url)
    # ---添加用户代理--- #
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    # ---添加用户代理--- #
    # ---捕获网页不存在等一些异常--- #
    try:
        # ---将网页进行解码--- #
        resp = urllib.request.urlopen(request)
        cs = resp.headers.get_content_charset()
        if not cs:
            print("use default charset utf-8")
            cs = charset
        # ---将网页进行解码--- #
        html = resp.read().decode(cs)
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retries=num_retries - 1)
    # ---捕获网页不存在等一些异常--- #
    return html


def crawl_sitemap(url):
    """
    网站地图爬虫
    :param url: http://www.baidu.com
    :return:
    """
    sitemap = download(url)
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    for link in links:
        html = download(link)


def crawl_site(url, max_errors=5):
    """
    根据 ID 爬取 用于别名抓取可以按规律进行爬取
    :param url: 抓取的url
    :param max_error: 最大连续错误次数
    :return:
    """
    num_errors = 0
    for page in itertools.count(1):
        pg_url = '{}{}'.format(url, page)
        html = download(pg_url)
        if html is None:
            num_errors += 1
            if num_errors == max_errors:
                break
        else:
            num_errors = 0


# ---链接爬虫--- #
def link_crawler(start_url, link_regex, robots_url=None, user_agent='wswp'):
    """
    从给定的start_url开始进行爬取, 并规则继续爬取匹配规则的链接
    :param start_url:
    :param link_regex:
    :return:
    """
    if not robots_url:
        robots_url = '{}/robots.txt'.format(start_url)
    rp = get_robots_parser(robots_url) # 获取robot.txt 的parser(解析器)
    crawl_queue = [start_url]
    seen = set(crawl_queue)  # 设置以抓取过的页面记录，防止重复抓取
    while crawl_queue:
        url = crawl_queue.pop()
        if rp.can_fetch(user_agent,url):  # 如果指定的代理能够访问网页
            html = download(url)
            if html is None:
                continue
            # filter for links matching our regular expression
            for link in get_links(html):
                if re.search(link_regex, link) and not re.search('(login\?|register\?)',link):
                    # 生成绝对路径，方式被相对路径打断抓取
                    abs_link = urljoin(start_url, link)
                    if abs_link not in seen:  # 判断此链接是否已被抓取过
                        seen.add(abs_link)
                        crawl_queue.append(abs_link)
        else:
            print('Blocked by robots.txt:', url)


def get_links(html):
    """
    返回一个从html中获取的链接列表
    :param html:
    :return:
    """
    # webpage_regex = re.compile("""<a[^>] + href=["'](.*?)["']""", re.IGNORECASE)  # 忽略大小写 相当于re.I
    webpage_regex = re.compile("""<a href=["'](.*?)["']""", re.IGNORECASE)  # 忽略大小写 相当于re.I
    return webpage_regex.findall(html)


# ---链接爬虫--- #

def get_robots_parser(robots_url):
    """ return the robots parser object using the robots_url"""
    rp = robotparser.RobotFileParser()
    rp.set_url(robots_url)
    rp.read()
    return rp


# url = 'https://www.meetup.com'
# url = 'http://httpstat.us/500'
# url = 'http://example.python-scraping.com/sitemap.xml'
# print(download(url))
# crawl_sitemap(url)
# url = 'http://example.python-scraping.com/view/-'
# crawl_site(url)
url = 'http://example.python-scraping.com'
link_regex = '/(index|view)(/|)'
link_crawler(url, link_regex)
