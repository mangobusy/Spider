from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from lxml import etree
from time import sleep
'''
browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
input = browser.find_element(by=By.ID,value='kw')   # 定位输入框
input.send_keys('邓紫棋')   # 输入关键词
btn = browser.find_element(by=By.ID,value='su')  # 定位搜索按钮
btn.click()  # 点击搜索按钮
sleep(3)
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(3)
# 回退一个页面
browser.back()
sleep(3)
# 前进一个页面
browser.forward()
sleep(3)
# 关闭页面
browser.close()'''

# http://wjw.sz.gov.cn/yqxx/
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
browser = webdriver.Chrome(options=options)
browser.get('www.baidu.com')
print(browser.page_source)
browser.quit()