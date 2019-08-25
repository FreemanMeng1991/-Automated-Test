#!/usr/bin/envpython
##_*_coding:utf-8_*_
import time
from os import walk
from selenium import webdriver
from password import psw
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
#driver.maximize_window()
driver.get("https://en.mail.qq.com/cgi-bin/loginpage")
driver.switch_to.frame("login_frame")
driver.find_element_by_id("switcher_plogin").click() #切换登录方式
#输入账号密码
driver.find_element_by_id("u").clear()
driver.find_element_by_id("u").send_keys("1536854522")
driver.find_element_by_id("p").clear()
driver.find_element_by_id("p").send_keys(psw)
driver.find_element_by_id("login_button").click()

time.sleep(1) #稍等一会儿，让页面加载完全，再点击写信
driver.find_element_by_xpath("//*[@id='composebtn']").click() 
driver.switch_to.frame("mainFrame")
#填写收件人
driver.find_element_by_xpath("//*[@id='toAreaCtrl']/div[2]/input").send_keys("1536854522@qq.com")
driver.find_element_by_id("subject").send_keys("Automated Test")  #主题
#切换至正文编辑区域，注意这个区别包含在一个框架中，但是这个框架的id不是固定的，
#因此使用相对固定的scrolling 和 class 两个属性联合作为定位符
frame_body = driver.find_element_by_xpath('//iframe[@scrolling="auto" and @class="qmEditorIfrmEditArea"]')
driver.switch_to.frame(frame_body)
time.sleep(1)
driver.find_element_by_xpath("/html/body").send_keys("For Test")
time.sleep(1)
#从正文输入框所在的frame退回到大的iframe框架再上传附件
driver.switch_to.parent_frame() 
#遍历包含附件的文件夹，然后逐个上传
att_folder = r"C:\Users\FREEMAN\Desktop\utmp"
for root,dirs,files in walk(att_folder):
	for f in files:
		path = "\\".join([root,f])
		driver.find_element_by_name('UploadFile').send_keys(path)  #上传附件，注意修改附件地址
time.sleep(1)
driver.find_element_by_link_text("发送").click()








