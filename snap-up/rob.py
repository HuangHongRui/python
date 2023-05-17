import pdb
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

dir = '/Users/leo/mine/python/snap-up/chromedriver'

def open_chrome():
  options = webdriver.ChromeOptions()
  options.add_experimental_option('detach', True)#不自动关闭浏览器
  # options.add_argument('--start-maximized')    #浏览器窗口最大化
  browser = webdriver.Chrome(options=options)

  # 前往登录页&扫码
  browser.get('https://login.taobao.com')
  browser.find_element(By.XPATH, '//*[@class="iconfont icon-qrcode"]').click()

  # 停顿15秒，扫码登录
  time.sleep(10)  

  # 跳转到购物车页面
  browser.get("https://cart.taobao.com/cart.htm")

  # 如果不能勾选，则刷新
  # 如果能勾选，则跳出循环

  # 勾选所有
  browser.find_element(By.ID, "J_SelectAll1").click()

  # 点击结算
  browser.find_element(By.ID, "J_Go").click()

  # 勾选协议

  # 确定结算

  pdb.set_trace()



# 打开Chrome
if __name__ == '__main__':
  open_chrome()