from selenium import webdriver
import string
import time

browser = webdriver.Chrome(executable_path="C:\\test\\ChromeDriver.exe")
browser.delete_all_cookies()
browser.get('https://www.buyme.co.il/')
browser.find_element_by_class_name('seperator-link').click()
browser.find_element_by_class_name('text-btn').click()

browser.find_element_by_xpath('//*[@id="ember558"]/div/div[1]/div/div/div[3]/p/span').click()
browser.find_element_by_id('ember986').send_keys("nivtol@gmail.com")
browser.find_element_by_id('ember988').send_keys("London10")
browser.find_element_by_class_name('ui-btn').click() # click on כניסה BUYME


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

time.sleep(1)
browser.find_element_by_id('ember1175').send_keys("200") # הכנסה ש200
browser.find_element_by_xpath('//*[@id="ember1174"]/div[2]/div/button').click() # save button
browser.implicitly_wait(10)
browser.find_element_by_id('ember1249').clear()
browser.find_element_by_id('ember1249').send_keys("דניאל")
browser.find_element_by_id('ember1259_chosen').click()
browser.find_element_by_xpath('//*[@id="ember1259_chosen"]/div/ul/li[2]').click()
browser.find_element_by_xpath('//*[@id="ember1273"]/textarea').clear()
browser.find_element_by_xpath('//*[@id="ember1273"]/textarea').send_keys("מזל טוב אח שלי היקר")
browser.find_element_by_xpath('//*[@id="ember1215"]/div[4]/div/div[1]/div[2]/div/button').click() # click on mail icon
browser.delete_all_cookies()
#browser.find_element_by_xpath('//*[@id="ember1281"]').send_keys(Imagepath = "C:\test\hb.jpg") # image
#browser.find_element_by_xpath('//html/body/button').click() #image
time.sleep(2)
browser.find_element_by_class_name('btn-save').click() # שמירה
#browser.find_element_by_id('ember1710').clear();
#browser.find_element_by_id('ember1710').send_keys("danielg@gmail.com") # field of insert the mail
browser.find_element_by_xpath('//*[@id="ember1215"]/div[5]/button').click()# תשלום
time.sleep(3)
browser.close()



