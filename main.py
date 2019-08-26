from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import os
import urllib.parse

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

def tagatack(tagname):
    tagserachurl = "https://www.instagram.com/explore/tags/"
    targeturl = tagserachurl + urllib.parse.quote(tagname) + "/" #日本語をエンコードしてる
    driver.get(targeturl)
    time.sleep(10)

    print("now on #{}".format(tagname))

    #画像のリンクが　div._9AhH0　にあるようです。
    mediaList = []
    likedCounter = 0
    followCounter = 0

    mediaList = driver.find_elements_by_css_selector("div._9AhH0")
    mediaCounter = len(mediaList)
    # print(mediaCounter)
    for media in mediaList:
        media.click()
        # 次へボタンが表示される間はずっと回る
        while True:
            try:
                #30秒に一回実行するようにしたいテスト時は削除
                time.sleep(30)
                # time.sleep(5)

                # いいねの実行処理。今はタグ毎に30個で制限してる
                if likedCounter < 30:
                    driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span").click() #fav
                    likedCounter += 1
                    print("like {}".format(likedCounter))
                else:
                    # 結果出力
                    print("#{1} の投稿の{0}個をいいねしました。{2}人フォローしました。".format(likedCounter,tagname,followCounter))
                    break

                # フォローの実行処理。今はタグ毎に6個制限している
                # if followCounter <= 6:
                #     driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[2]/button").click() #follow
                #     followCounter += 1
                #     print("follow {}".format(followCounter))
                #     time.sleep(5)
                #     #既フォローの場合の処理
                #     try:
                #         driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
                #     except:
                #         pass

                time.sleep(5)
                
                
                # 次へボタンをおす
                driver.find_element_by_css_selector("a.HBoOv.coreSpriteRightPaginationArrow").click()


            except:
                break
        break
        


if __name__ == '__main__':

    # ログインからトップページ表示までの処理
    driver.get('https://www.instagram.com/')
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a').click()
    time.sleep(3)
    driver.find_element_by_name('username').send_keys(os.environ['INSTAID'])
    driver.find_element_by_name('password').send_keys(os.environ['INSTAPASS'])
    driver.find_element_by_name('password').send_keys(Keys.RETURN)
    time.sleep(3)

    # taglistの中の順番に実行
    taglist = ["ファインダー越しの私の世界","impression_shots","indy_photolif","photosq_jp","pics_jp"]
    for tag in taglist:
        tagatack(tag)

    # driver.quit()

