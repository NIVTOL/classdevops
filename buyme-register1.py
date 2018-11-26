from selenium import webdriver
import random
import string
import time

browser = webdriver.Chrome(executable_path="C:\\test\\ChromeDriver.exe")
browser.get('https://www.buyme.co.il/')
browser.find_element_by_class_name('seperator-link').click() # button הרשמה
browser.find_element_by_class_name('text-btn').click() # button פעם ראושנה BUYME


browser.find_element_by_id('ember973').send_keys("niv")
browser.find_element_by_id('ember975').send_keys("nivtol@gmail.com")
browser.find_element_by_id('valPass').send_keys("London10")
browser.find_element_by_id('ember979').send_keys("London10")


browser.find_element_by_xpath ('//*[@id="ember980"]/label/i').click() # checkbox mark
browser.find_element_by_xpath ('//*[@id="ember982"]/label/i').click() #uncheck the check box privacy
browser.find_element_by_xpath ('//*[@id="ember971"]/button').click() # click submit

time.sleep(1101)
browser.close()

