# Web Scraping With Python
《用Python学习网络爬虫》学习记录

```
# 使用detectem
docker pull scrapinghub/splash
pip install detectem
$ det http://example.python-scraping.com
# output
[('juuery','1.11.0')]
```

```
docker pull wappalyzer/cli
docker run wappalyzer/cli http://example.python-scraping.com
docker run wappalyzer/cli http://example.python-scraping.com
```
输出
```json
{
    "urls": [
        "http://example.python-scraping.com/"
    ],
    "applications": [
        {
            "name": "Modernizr",
            "confidence": "100",
            "version": "2.7.1",
            "icon": "Modernizr.svg",
            "website": "https://modernizr.com",
            "categories": [
                {
                    "12": "JavaScript Frameworks"
                }
            ]
        },
        {
            "name": "Nginx",
            "confidence": "100",
            "version": "1.12.2",
            "icon": "Nginx.svg",
            "website": "http://nginx.org/en",
            "categories": [
                {
                    "22": "Web Servers"
                }
            ]
        },
        {
            "name": "Bootstrap",
            "confidence": "100",
            "version": "",
            "icon": "Bootstrap.svg",
            "website": "https://getbootstrap.com",
            "categories": [
                {
                    "18": "Web Frameworks"
                }
            ]
        },
        {
            "name": "Web2py",
            "confidence": "100",
            "version": "",
            "icon": "Web2py.png",
            "website": "http://web2py.com",
            "categories": [
                {
                    "18": "Web Frameworks"
                }
            ]
        },
        {
            "name": "jQuery",
            "confidence": "100",
            "version": "1.11.0",
            "icon": "jQuery.svg",
            "website": "https://jquery.com",
            "categories": [
                {
                    "12": "JavaScript Frameworks"
                }
            ]
        },
        {
            "name": "Python",
            "confidence": "0",
            "version": "",
            "icon": "Python.png",
            "website": "http://python.org",
            "categories": [
                {
                    "27": "Programming Languages"
                }
            ]
        }
    ],
    "meta": {
        "language": "en"
    }
}
```
