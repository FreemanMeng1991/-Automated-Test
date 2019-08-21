#!/usr/bin/envpython
#_*_coding:utf-8_*_
#模拟百度搜索bilibil关键词
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC  

#Tips: 下载对应Chrome版本的chromedriver,下载地址如下
#http://chromedriver.storage.googleapis.com/index.html
#将其解压后与chrome.exe放在一起并将其路径添加至PATH
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
input_Element = driver.find_element_by_id("kw")
input_Element.send_keys("bilibili")
input_Element.submit()
try:
	#等10秒，若标题栏中不出现 "bilibili" 字样则抛出异常
	#这里是显式等待，注意显式与隐式等待不可混用！
	WebDriverWait(driver, 10).until(EC.title_contains("bilibili"))
	# You should see "bilibili_百度搜索"
	print(driver.title)
finally:
    pass

