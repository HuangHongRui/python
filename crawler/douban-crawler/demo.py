import requests
from bs4 import BeautifulSoup

def crawl(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }
    # 发起HTTP请求并获取响应内容
    response = requests.get(url, headers=headers)
    content = response.text
    
    # 解析HTML内容
    soup = BeautifulSoup(content, 'html.parser')
    
    # 提取数据
    # 这里以提取页面中的所有链接为例
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        print(href)

# 测试爬虫
crawl('https://www.baidu.com')