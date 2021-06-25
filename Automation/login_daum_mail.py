import os.path as p
from selenium import webdriver
import json
from pathlib import Path 


BASE_DIR=Path(__file__).resolve().parent.parent
_login_info=p.join(BASE_DIR,'Secrets/login_info.json')

with open(_login_info,'r') as login_info:
    info=json.loads(login_info.read())


driver=webdriver.Chrome("./chromedriver")
driver.implicitly_wait(3)

driver.get('https://mail.daum.net/')
driver.find_element_by_xpath('//*[@id="daumHead"]/div/div/a[4]/span').click()
driver.find_element_by_xpath('//*[@id="mArticle"]/div[1]/div/div/div[2]/a[1]').click()

driver.find_element_by_name('email').send_keys(info['id'])
driver.find_element_by_name('password').send_keys(info['password'])
driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button[1]').click()

driver.implicitly_wait(20)

driver.find_element_by_xpath('//*[@id="folder"]/div/div/div[1]/ul/li[6]/a[1]').click()

driver.implicitly_wait(3)
titles=driver.find_elements_by_css_selector('strong.tit_subject')

for title in titles:
    print(title.text)
