from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import os

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

# ポップアップの存在確認
try:
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()    
except:
    pass

# 検索窓に文字列入力
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys("#文字列", Keys.RETURN)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(Keys.RETURN)
    

time.sleep()
driver.quit()