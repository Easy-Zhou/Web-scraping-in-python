#!/anaconda3/bin/python
# @Time    : 2019-04-10 13:04
# @Author  : zhou
# @File    : downloadweb
# @Software: PyCharm
# @Description: 

import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError


def download(url, user_agent='wswp', num_retries=2, charset='utf-8'):
    """
    下载网页
    :param url: 网页地址
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


# url = 'https://www.meetup.com'
url = 'http://httpstat.us/500'
print(download(url))
