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
time.sleep(5)

#画像のリンクが　div._9AhH0　にあるようです。
mediaList = []
likedCounter = 0
followcounter = 0

mediaList = driver.find_elements_by_css_selector("div._9AhH0")
mediaCounter = len(mediaList)
print(mediaCounter)
for media in mediaList:
    media.click()
    # 次へボタンが表示されるまで
    while True:
        try:
            time.sleep(5)
            driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span").click() #fav
            driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[2]/button").click() #follow

            time.sleep(5)
            likedCounter += 1
            followcounter += 1
            print("liked {} of {}".format(likedCounter,mediaCounter))
            # driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/a").click()
            driver.find_element_by_css_selector("a.HBoOv.coreSpriteRightPaginationArrow").click()
        except:
            break
    break



time.sleep(3)
# driver.quit()