from selenium import webdriver
import random
import string
import time

browser = webdriver.Chrome(executable_path="C:\\test\\ChromeDriver.exe")
browser.get('https://www.buyme.co.il/')


browser.find_element_by_id('ember650_chosen').click() # choose סכום
browser.find_element_by_xpath('//*[@id="ember650_chosen"]/div/ul/li[4]').click() # 199-299

browser.find_element_by_id('ember674_chosen').click() # choose אזור
browser.find_element_by_xpath('//*[@id="ember674_chosen"]/div/ul/li[3]').click() # מרכז

browser.find_element_by_id('ember641_chosen').click() # choose ssאזור
browser.find_element_by_xpath('//*[@id="ember641_chosen"]/div/ul/li[2]').click()
browser.find_element_by_class_name('ui-btn').click()#test3387659