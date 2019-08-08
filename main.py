from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import os
import urllib.parse

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.get('https://www.instagram.com/')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a').click()
time.sleep(3)

usernameField = driver.find_element_by_name('username')
usernameField.send_keys(os.environ['INSTAID'])
passwordField = driver.find_element_by_name('password')
passwordField.send_keys(os.environ['INSTAPASS'])
passwordField.send_keys(Keys.RETURN)

time.sleep(3)


tag = "ファインダー越しの私の世界"
tagserachurl = "https://www.instagram.com/explore/tags/"
targeturl = tagserachurl + urllib.parse.quote(tag) + "/" #日本語をエンコードしてる
driver.get(targeturl)



    


time.sleep()
driver.quit()