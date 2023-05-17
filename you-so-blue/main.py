import pdb
import time
import random
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def get_random_ua():
  ua = UserAgent()
  return ua.random

url = 'https://www.nihaowua.com/'
headers = {'User-Agent': get_random_ua()}

# 获取一句污言
def get_blue_text():
  try:
    response = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(response.text)
    text = soup.find('section').text.strip()
    return text
  except:
    print('获取污言失败')

# 获取N句污言
def get_blue_list(num = 1):
  text_list = []
  try_time = 0

  while True:
    # 随机延迟1~3秒
    time.sleep(random.randint(1, 3))

    try:
      text = get_blue_text()
    except:
      try_time += 1
      if try_time < 5:
        continue
      else:
        break

    text_list.append(text)
    if len(text_list) >= num:
      break

  return text_list

# 存储文件
def save_file(text_list):
  try:
    with open('blue.md', 'a') as f:
      for text in text_list:
        f.write(text + '\n')
  except:
    print('存储文件失败')

if __name__ == '__main__':
  blue_list = get_blue_list(5)
  save_file(blue_list)
  print(blue_list)
