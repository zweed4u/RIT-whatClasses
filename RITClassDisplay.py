import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


username=raw_input("MyCourses Username? ")
passw=raw_input("Password? ")
#Sorry for the plaintext. Will update.

path_to_driver=os.getcwd()+'/phantomjs'
browser = webdriver.PhantomJS(executable_path = path_to_driver)
browser.delete_all_cookies()
browser.get('https://mycourses.rit.edu/index.asp')

user = browser.find_element_by_name('username')
password = browser.find_element_by_name('password')
LOGIN_BUTTON_XPATH ='//*[@id="login_box"]/form/div[3]/input'

user.send_keys(str(username).lower())
password.send_keys(passw)
button = browser.find_element_by_xpath(LOGIN_BUTTON_XPATH)
button.click()
print "\nLogging in...\n"

##~~Screenshots for error checking~~##
#browser.save_screenshot("login.png")
#time.sleep(1)
#browser.save_screenshot("login2.png")

##~~Easy way to find what we need but not expandable~~##
#CURRENT_CLASS_LIST = browser.find_element_by_class_name('d2l-datalist')
#print CURRENT_CLASS_LIST.text

numClasses = raw_input("Number of classes? ")

for i in range(int(numClasses)):
	#Get each with partial xPath names
	print  "\nClass " + str(i+1) + ": " + browser.find_element_by_xpath("//*[starts-with(@id, 'd2l_2_')]/ul/li["+str(i+1)+"]/div[1]/div/a").text
