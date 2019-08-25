#!/usr/bin/envpython
#_*_coding:utf-8_*_
#自动化设置百度搜索偏好
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.action_chains import ActionChains

#Tips: 下载对应Chrome版本的chromedriver,下载地址如下
#http://chromedriver.storage.googleapis.com/index.html
#将其解压后与chrome.exe放在一起并将其路径添加至PATH
email = "1536854522@qq.com"
psw   = "helloworld123"
name  = "汪藏海"
sex   = 'm'
tele  = '18739639472'
birthday = "1980-1-23"
enroll   = "1990-10"
school_name = '商丘科技大学'
major = '考古'
addr  = '开封'
workyear = '2002'
salary  = '100'
driver = webdriver.Chrome()
driver.get("https://www.51job.com/")
driver.find_element_by_id("sign_btn").click() #sign-up
try:
	driver.find_element_by_link_text("邮箱注册 >").click()
	time.sleep(0.5) #让页面有时间加载完毕
	#输入账号、密码、确认密码
	driver.find_element_by_id("useremail").send_keys(email)
	driver.find_element_by_id("userpwd").send_keys(psw)
	driver.find_element_by_id("cfmpwd").send_keys(psw)
	driver.find_element_by_id("isread_em").click()
	driver.find_element_by_id("submitbtn").click()
	try:
		#如果该邮箱已被注册，则存在email_err元素，点击直接登录
		driver.find_element_by_xpath("//*[@id='email_err']/a").click()
		time.sleep(0.5)
		driver.find_element_by_id("password").send_keys(psw)
		driver.find_element_by_id("login_btn").click()
	except:
		pass
finally:
	print("Successfully sign-up and log-in !")
	time.sleep(0.5)
	try:
		#针对已注册但没有创建简历的用户，会出现创建简历的链接，点击创建简历
		##新用户注册，则直接跳转至简历填写页面，不会出现创建简历的链接
		driver.find_element_by_xpath("//*[@class='resume']/div/p/a").click()
	except:
		pass

try: 
	#若没有创建简历，则转到填写基本信息的页面
	driver.find_element_by_id("base_name").send_keys(name)
	if(sex.lower() == 'm'): #性别
		driver.find_element_by_id("base_sex_0").click()

	"""
	填写生日信息，注意3个要点：
	1. 填写生日的输入框是只读的，不能直接使用send_keys，先用js移除readonly属性后再填写。
	2. 这个输入框下面还隐藏着一个输入框，其中的内容才是真正提交的内容，因此需通过js代码
	   定位到这个输入框并再此填写真正的生日，只填写1中所述的输入框在提交时会提示没有输入生日！
	   注意：填写时可以一直保持这个输入框处于隐藏状态
	3. 上述两个输入框中的日期格式是不同的，需要做适当调整。
	"""
	js = 'document.getElementById("base_birthday_input").removeAttribute("readonly");'
	driver.execute_script(js)	#移除readonly属性
	driver.find_element_by_id("base_birthday_input").send_keys(birthday) 
	#使用js填写隐藏输入框并调整输入格式
	js = "document.getElementById('base_birthday').value='_date_here';" 
	driver.execute_script(js.replace("_date_here",birthday.replace("-","/")))


	#填写工作年限,原理同上
	js = 'document.getElementById("base_workyear_input").removeAttribute("readonly");'
	driver.execute_script(js)
	driver.find_element_by_id("base_workyear_input").send_keys(workyear)
	js = "document.getElementById('base_workyear').value='_year_here';" 
	driver.execute_script(js.replace("_year_here",workyear))

	#填写手机，移除readonly和disabled属性，否则会弹出发送验证码页面
	js  = 'document.getElementById("tele").removeAttribute("readonly");'
	js2 = 'document.getElementById("tele").removeAttribute("disabled");'
	driver.execute_script(js)
	driver.execute_script(js2)
	driver.find_element_by_id("tele").send_keys(tele)

	#遍历所在地区时使用try的原因：有可能还没遍历到最后就找到了想要的选项
	#点选后，地区选择页面不复存在，造成后续元素无法找到，抛出异常，但这个
	#异常是可以忽略的，所以在except块中pass
	try:
		#先点击选择地区按钮id=base_area_click，弹出地区选择页面
		driver.find_element_by_id("base_area_click").click()
		time.sleep(0.5)
		#通过xpath获取左侧列表中所有列表元素
		groups = driver.find_elements_by_xpath("//*[@id='base_area_click_center_left']/li")
		for grp in groups:
			grp.click() #依次点击弹出页面左侧所有的地区分类列表
			grp_id = grp.get_attribute("id") #获取左侧地区分类列表中每个条目的id
			time.sleep(0.5)
			#获取左侧列表中各地名分类对应的右侧地名表格的id，查看网页源代码即知其id规律
			area_table_id = grp_id.replace("left_each","right_list") 
			table = driver.find_element_by_id(area_table_id) #获取地名表格
			rows = table.find_elements_by_tag_name("tr") #获取表格所有行
			for row in rows: #遍历表格中单元格，发现匹配项后点击
				cells = row.find_elements_by_tag_name("td") #获取一行中的所有单元格
				for cell in cells:  
					if(addr in cell.text):#检测单元格中是否包含该地区名称
						#获取对应地区元素的id
						province_id = cell.find_element_by_tag_name("em").get_attribute("id")
						#print(addr,cell.text,province_id)
						driver.find_element_by_id(province_id).click()	
	except: pass	

	#年薪
	driver.find_element_by_id("sal_salary").send_keys(salary)

	#入学时间，原理同输入生日
	js = 'document.getElementById("edu_timefrom_input").removeAttribute("readonly");'
	driver.execute_script(js)
	driver.find_element_by_id("edu_timefrom_input").send_keys(enroll)
	js = "document.getElementById('edu_timefrom').value='_timefrom_here';" 
	driver.execute_script(js.replace("_timefrom_here",enroll.replace("-","/")))

	"""
	选择文化程度：
	Way1:
	根据网页源代码，不同的文化程度对应于不同的编号，编号被填写在文化程度输入框下
	的一个隐藏的输入框edu_degree之中。先使其可见，再填入相应编号后，使用click点击
	edu_degree输入框上面的edu_degree_list输入框，即可完成填写。
	"""
	# WebDriverWait(driver,10,0.1).until(EC.presence_of_element_located((By.ID,'edu_degree')))
	# js = "document.getElementById('edu_degree').type='block';"
	# driver.execute_script(js)
	# driver.find_element_by_id("edu_degree").send_keys(6)
	# driver.find_element_by_xpath("//*[@id='edu_degree_list']/input").click()
	# time.sleep(0.5)


	"""
	选择文化程度：
	Way2:(Preffered)
	使用ActionChains模拟"鼠标点击输入框->向下滑动->选中某一选项->点击确定"这一过程
	"""
	degree_input = driver.find_element_by_xpath("//*[@id='edu_degree_list']/input")
	degree = driver.find_element_by_xpath("//*[@id='edu_degree_list']/div/span[6]")
	ac = ActionChains(driver)
	ac.click(degree_input)
	ac.move_to_element(degree)
	ac.click(degree)
	ac.perform()


	#学校名
	driver.find_element_by_id("edu_schoolname").send_keys(school_name) 

	#输入专业名，这里采用自定义专业名的方法。先输入专业名，然后网页弹出自定义专业选项
	#点击后进入选择页面，先选大类，再填专业名（已自动填入），最后点确定
	driver.find_element_by_id("edu_major_input").send_keys(major)
	driver.find_element_by_id("edu_majordes_selfdefine_click").click() #点击自定义专业
	time.sleep(0.5)
	#选择专业大类别
	driver.find_element_by_xpath("//*[@class='ttag edu_major_input_association_each_click'][4]").click()
	driver.find_element_by_id("edu_majordes_selfdefine_button").click()

	#点击"下一步"按钮，一旦正确填写完所有基本信息，再次登录时就不会出现填写基本信息的页面！
	#driver.find_element_by_xpath("//*[@class='btm']/span").click()
	#sys.exit(-1)
except:
	print("base_country_click_center_rightResume already exist!")
	driver.find_element_by_xpath("//*[@class='btnbox']/span[2]").click()
	
	driver.switch_to.window(driver.window_handles[-1])  # driver切换至最新生产的页面句柄
	time.sleep(0.5)
	
	basic = driver.find_element_by_id("Basic")
	ac = ActionChains(driver)
	ac.move_to_element(basic).perform()	# 鼠标悬浮
	time.sleep(0.5)

	#展开更多简历细节
	driver.find_element_by_id("basedetail_edit").click()
	driver.find_element_by_class_name("mbox").click()

	#选择婚姻状况
	#这是使用ActionChains实现下拉列表选取的一个例子
	driver.find_element_by_id("base_marriage_list").click()
	option = driver.find_element_by_xpath("//*[@id='base_marriage_list']/div/span[2]")
	ac = ActionChains(driver)
	ac.move_to_element(option)
	ac.click(option)
	ac.perform()
	time.sleep(0.5)

	driver.find_element_by_id("base_idcard").clear() #先清空，防止在尾部增量填写
	driver.find_element_by_id("base_idcard").send_keys("410205197901230519")

	
	#ActionChains操作下拉列表
	driver.find_element_by_id("base_politicsstatus_list").click()
	option = driver.find_element_by_xpath("//*[@id='base_politicsstatus_list']/div/span[2]")
	ac = ActionChains(driver)
	ac.move_to_element(option)
	ac.click(option)
	ac.perform()
	time.sleep(0.5)

	driver.find_element_by_id("base_stature").send_keys("178")
	driver.find_element_by_id("base_address").clear()#先清空，防止在尾部增量填写
	driver.find_element_by_id("base_address").send_keys("开封市示范区第五大街北段")
	driver.find_element_by_id("base_stature").send_keys("178")

	#通过js移除输入框的disabled特性，绕过手机验证码环节
	js = 'document.getElementById("tele").removeAttribute("disabled");'
	driver.execute_script(js)
	driver.find_element_by_id("tele").send_keys(tele)

	#两次确认
	driver.find_element_by_id("basedetail_save").click()
	driver.find_element_by_id("basedetail_confirm_").click()

	driver.find_element_by_id("education_new").click()
	js = 'document.getElementById("edu_timefrom_input").removeAttribute("readonly");'
	driver.execute_script(js)	#移除readonly属性
	driver.find_element_by_id("edu_timefrom_input").send_keys("2013-9") 
	#使用js填写隐藏输入框并调整输入格式
	js = "document.getElementById('edu_timefrom').value='2013/9';" 
	driver.execute_script(js)

	js = 'document.getElementById("edu_timeto_input").removeAttribute("readonly");'
	driver.execute_script(js)	#移除readonly属性
	driver.find_element_by_id("edu_timeto_input").clear()
	driver.find_element_by_id("edu_timeto_input").send_keys("2016-6") 
	#使用js填写隐藏输入框并调整输入格式
	js = "document.getElementById('edu_timeto').value='2016/6';" 
	driver.execute_script(js)

	driver.find_element_by_id("edu_schoolname").send_keys("商丘建桥大学")
	
	#选择文化程度：另一种点选下拉列表的方法，这种更为直接
	driver.find_element_by_xpath("//*[@id='edu_degree_list']/input").click()
	time.sleep(0.5)
	driver.find_element_by_xpath("//*[@id='edu_degree_list']/div/span[7]").click()
	
	driver.find_element_by_id("edu_major_click").click()
	mjr_categories = driver.find_elements_by_xpath("//*[@id='edu_major_click_center_left']/li")
	try:
		for cat in mjr_categories:
			cat.click()
			cat_id = cat.get_attribute("id")
			print(cat_id)
			major_tbl = cat_id.replace("left_each","right_list")
			table = driver.find_element_by_id(major_tbl)
			rows = table.find_elements_by_tag_name("tr")
			for row in rows:
				cells = row.find_elements_by_tag_name("td")
				for cell in cells:
					major_list  = cell.find_element_by_tag_name("em").click()
					list_id     = cell.find_element_by_tag_name("em").get_attribute("id")
					sub_list_id = list_id.replace("_list_","_list_sub_")
					sub_list    = driver.find_element_by_id(sub_list_id).find_elements_by_tag_name('span')
					for major in sub_list:
						print(major.text)
						if ("软件工程" in major.text):
							major.click()
	except: pass

	driver.find_element_by_id("edu_describe").send_keys("我在搬砖")
	driver.find_element_by_id("education_save_").click()

	driver.find_element_by_id("additionattach_new").click()
	driver.find_element_by_id("atta_name").send_keys("盗墓笔记")
	driver.find_element_by_id("atta_uploadtype_list").click()
	driver.find_element_by_xpath("//*[@id='atta_uploadtype_list']/div/span[1]").click()
	driver.find_element_by_id("atta_uploadfile").send_keys(r"C:\Users\FREEMAN\Desktop\test.xls")
	driver.find_element_by_id("atta_describe").send_keys("战国帛书")
	

	


	
	
	