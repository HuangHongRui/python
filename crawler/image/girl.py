import os
import time
import requests
import numpy as np
from lxml import html
from bs4 import BeautifulSoup

headers = {
  'Referer': 'http://girl-atlas.com/',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

# 初始URL http://girl-atlas.com/
# 访问每个页面，获取每个页面的专辑URL
# 返回列表，包含所有专辑URL
def  get_page_url():
  try_times = 0
  page_num = 1
  album_url = []
  page_url = 'http://girl-atlas.com/?p='

  while True:
    time.sleep(np.random.rand() * 5)

    try:
      res = requests.get(page_url + str(page_num), headers = headers)
    except:
      continue
      print('访问错误')

    soup = BeautifulSoup(res.text)
    list_soup = soup.findAll('div', {'class': 'album-item row'})
    try_times += 1

    if list_soup == None and try_times < 5:
      continue
    elif list_soup == None or len(list_soup) <= 1:
      break 

    try:
      for album_info in list_soup:
        album_href = album_info.find('h2').find('a').get('href')
        if not album_href:
          continue
        album_url.append(album_href)
    except:
      print('获取专辑url错误')

    page_num += 1
    try_times = 0

  return album_url

# 返回列表，包含所有Girl的字典
def get_album_image(page_url):
  girl_list = []
  # http://girl-atlas.com/album/576545f358e039318beb3dbb
  for url in page_url:
    time.sleep(np.random.rand() * 5)
    try:
      res = requests.get('http://girl-atlas.com' + url, headers = headers)
      parsed_body = html.fromstring(res.text)
      girl_title  = parsed_body.xpath('//title/text()')
      image_urls = parsed_body.xpath('//li[@class="slide "]/img/@src | //li[@class="slide "]/img/@delay')
      girl_dict = {girl_title[0]: image_urls}
      girl_list.append(girl_dict)
    except Exception as e:
      print('访问错误: ', e)

  return girl_list

# 对列表进行遍历，下载图片
def down_image(girl_list):
  count = 1
  start_dir = './file/'

  for girl in girl_list:
    dir_name = start_dir + list(girl.keys())[0]
    urls = list(girl.values())[0]

    if not os.path.exists(dir_name):
      os.makedirs(dir_name)

    for url in urls:
      try:
        with open(dir_name + '/' + url.split('/')[-1].split('!')[0], 'wb') as f:
          r = requests.get(url, headers=headers)
          f.write(r.content)
      except:
        continue

    count += 1
    print (count, list(girl.keys())[0] + "  done!!!")

if __name__ == '__main__':

  page_url = get_page_url()
  girl_list = get_album_image(page_url)
  down_image(girl_list)