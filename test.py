from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get('https://netpeak.ua/')
test_career = driver.find_element_by_link_text('Карьера').click()
time.sleep(10)

driver.close()
driver.quit()

driver = webdriver.Chrome()
driver.get('https://career.netpeak.group/')
work_career = driver.find_element_by_link_text('Я хочу работать в Netpeak').click()
time.sleep(2)
name_input = driver.find_element_by_id('inputName')
name_input.send_keys("qweerryy")
time.sleep(1)
lastname = driver.find_element_by_id('inputLastname')
lastname.send_keys('asdfgh')
time.sleep(1)
email = driver.find_element_by_id('inputEmail')
email.send_keys('qwerty')
time.sleep(1)
email.send_keys(Keys.ENTER)
time.sleep(5)
kurs_career = driver.find_element_by_link_text('Курсы').click()
print(driver.current_url)

driver.close()
driver.quit()