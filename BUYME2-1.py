from selenium import webdriver
import random
import string
import time
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(executable_path="C:\\test\\ChromeDriver.exe")
browser.delete_all_cookies()
browser.get('https://www.buyme.co.il/')
browser.find_element_by_class_name('seperator-link').click()
browser.find_element_by_class_name('text-btn').click()
#//*[@id="ember558"]/div/div[1]/div/div/div[3]/p/span
browser.find_element_by_xpath('//*[@id="ember558"]/div/div[1]/div/div/div[3]/p/span').click()
browser.find_element_by_id('ember986').send_keys("nivtol@gmail.com")
browser.find_element_by_id('ember988').send_keys("London10")
browser.find_element_by_class_name('ui-btn').click() # click on כניסה BUYME
#browser.implicitly_wait(10) #stop in level of driver

time.sleep(2)

browser.find_element_by_id('ember650_chosen').click() # choose סכום
browser.find_element_by_xpath('//*[@id="ember650_chosen"]/div/ul/li[4]').click() # 199-299

browser.find_element_by_id('ember665_chosen').click() # choose אזור
browser.find_element_by_xpath('//*[@id="ember665_chosen"]/div/ul/li[3]').click() # מרכז

browser.find_element_by_id('ember674_chosen').click() # choose אזור
browser.find_element_by_xpath('//*[@id="ember674_chosen"]/div/ul/li[2]').click() # גיפט קארד מותגי אופנה
time.sleep(1)
browser.find_element_by_class_name('ui-btn').click() # click on תמצא לי מתנה
time.sleep(5)
browser.find_element_by_id('ember1134').click() # opticana
#//*[@id="ember709"]
time.sleep(1)
browser.find_element_by_id('ember1175').send_keys("100") # הכנסה של 100
browser.find_element_by_xpath('//*[@id="ember1174"]/div[2]/div/button').click() # save button
time.sleep(5)

browser.delete_all_cookies()
browser.find_element_by_id('ember1249').send_keys("דניאל")
browser.find_element_by_id('ember1259_chosen').click()
browser.find_element_by_xpath('//*[@id="ember1273"]/textarea').send_keys("מזל טוב אח שלי היקר")
browser.find_element_by_id('ember1282').click()
#browser.find_element_by_xpath('//*[@id="ember1281"]').send_keys(Imagepath = "C:\test\hb.jpg")
#browser.find_element_by_xpath('//html/body/button').click()
#browser.find_element_by_class_name('btn-send-option-inner').click()
#browser.find_element_by_xpath('//*[@id="ember1215"]/div[4]/div/div[1]/div[2]/div/button').click() # click on mail icon
#browser.find_element_by_id('ember1710').send_keys("dan@gmail.com") # field of insert the mail
#browser.find_element_by_class_name('btn-save').click() #save the mail button
time.sleep(1)
#browser.find_element_by_xpath('//*[@id="ember1773"]/div[5]/button').click()
#browser.find_element_by_class_name('submit-wrapper').click() #save the mail button
#browser.find_element_by_xpath('//*[@id="ember1258"]/option[2]').click()
time.sleep(221)

#//*[@id="ember1258_chosen"]/a
# browser.find_element_by_xpath('//*[@id="ember1215"]/div[4]/div/div[1]/div[2]/div/button').click() # click on mail icon
# browser.find_element_by_id('ember1709').send_keys("danielgot@gmail.com") # field of insert the mail
# browser.find_element_by_class_name('btn-save').click() #save the mail button
# time.sleep(1)
# browser.find_element_by_id('ember1258_chosen').click()
# browser.find_element_by_xpath('//*[@id="ember1258"]/option[2]').click()
