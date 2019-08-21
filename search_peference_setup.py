#!/usr/bin/envpython
#_*_coding:utf-8_*_
#自动化设置百度搜索偏好
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.action_chains import ActionChains


#Tips: 下载对应Chrome版本的chromedriver,下载地址如下
#http://chromedriver.storage.googleapis.com/index.html
#将其解压后与chrome.exe放在一起并将其路径添加至PATH
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
input_Element = driver.find_element_by_id("kw")
input_Element.send_keys("bilibili")
input_Element.submit()
actions = ActionChains(driver)
print(dir(actions))
try:
	#等10秒，若标题栏中不出现 "bilibili" 字样则抛出异常
	#这里是显式等待，注意显式与隐式等待不可混用！
	WebDriverWait(driver, 10).until(EC.title_contains("bilibili"))
	# You should see "bilibili_百度搜索"
	print(driver.title)
	settings = driver.find_element_by_link_text("设置")
	settings.click()

	driver.find_element_by_link_text("搜索设置").click()
	time.sleep(0.5)
	
	prompt = driver.find_element_by_id("s1_2")
	prompt.click()

	srch_lang = driver.find_element_by_id("SL_1")
	srch_lang.click()
		
	choice = driver.find_element_by_id("nr")
	choice.find_element_by_xpath("//option[@value='50']").click()
	

	predict = driver.find_element_by_id("issw1")
	predict.find_element_by_xpath("//option[@value='2']").click()

	history = driver.find_element_by_id("sh_1")
	history.click()

	driver.find_element_by_link_text("保存设置").click()

	#点击对话框
	al = driver.switch_to_alert()
	time.sleep(0.5)
	al.accept()
finally:
    #driver.quit()
    pass

