from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import urllib.parse
import time
import os
import configparser


#configから情報読み出し
root_directory = os.getcwd()
c = configparser.ConfigParser()
configFilePath = os.path.join(root_directory, 'config.cfg')
c.read(configFilePath)

class Config:
    uid = c.get('userinfo', 'userid')
    pasu = c.get('userinfo', 'password')
    url = c.get('accessinfo', 'URL')
    lpath = c.get('accessinfo', 'loginPath')
    tag = c.get('accessinfo', 'tagName')
    serchurl = c.get('accessinfo', 'tagSearchURL')
    selector = c.get('accessinfo', 'mediaSelector')
    lxpath = c.get('accessinfo', 'likeXpath')
    nxpath = c.get('accessinfo', 'nextPagerSelector')


#headlessでchromwブラウザの立ち上げ
#options.add_argument('--headless')
options = Options()
options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
driver = webdriver.Chrome(chrome_options=options)

#ログイン処理
driver.get(Config.url)
time.sleep(3)
driver.find_element_by_xpath(Config.lpath).click()
time.sleep(3)
usernameField = driver.find_element_by_name('username')
usernameField.send_keys(Config.uid)
passwordField = driver.find_element_by_name('password')
passwordField.send_keys(Config.pasu)
passwordField.send_keys(Keys.RETURN)

#タグで検索をかけて表示
time.sleep(3)
encodedTag = urllib.parse.quote(Config.tag) #普通にURLに日本語は入れられないので、エンコードする
encodedURL = Config.serchurl.format(encodedTag)
print("encodedURL:{}".format(encodedURL))
driver.get(encodedURL)
#driver.quit()

#画像をクリック
mediaList = []
likedCounter = 0

time.sleep(3)
driver.implicitly_wait(10)
mediaList = driver.find_elements_by_css_selector(Config.selector)
mediaCounter = len(mediaList)
print("Found {} media".format(mediaCounter))
for media in mediaList:
    media.click()
    # 次へボタンが表示されるまで
    while True:
        try:
            time.sleep(3)
            driver.find_element_by_xpath(Config.lxpath).click()
            driver.implicitly_wait(10)
            likedCounter += 1
            print("liked {} of {}".format(likedCounter,mediaCounter))
            driver.find_element_by_css_selector(Config.nxpath).click()
        except:
            break
    break

print("You liked {} media".format(likedCounter))
