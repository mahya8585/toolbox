# reserveサイトをスクレイピングして、空席情報を取得する
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 検索条件定数
DATE = '20240101'
# max8人
PEOPLE = '8'
# TDL, TDS のみ選択可　複数選択可　ホテルは別restaurantタイプのため別途対応
PARK = ['TDL']
SCRAPE_URL = f'https://reserve.tokyodisneyresort.jp/restaurant/search/?useDate={DATE}&adultNum={PEOPLE}&childNum=0&childAgeInform=&nameCd=&wheelchairCount=0&stretcherCount=0&keyword=&reservationStatus=1'

# URLの作成
for park in PARK:
    if park == 'TDL':
        SCRAPE_URL += f'&restaurantType%5B0%5D=4'
    elif park == 'TDS':
        SCRAPE_URL += f'&restaurantType%5B1%5D=5'
    else:
        print('まだ対応していないPARKの値です。')
        exit()
print(SCRAPE_URL)

# ブラウザを開き、サイトにアクセス
print('access start')
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome()
browser.get(SCRAPE_URL)

time.sleep(20)

# 同意ボタンをクリック
print('click 同意')
browser.find_element(By.XPATH, '/html/body/div[6]/p[1]/a/img').click()

# Selection01 タグ内のテーブルのスタイルがnoneでないもののみを取得
print('get blank reservation')
restaurants = browser.find_elements(By.CLASS_NAME, 'hasGotReservation')

if len(restaurants) == 0:
    print('空席なし')
    exit()

for restaurant in restaurants:
    print(restaurant.text)

# ブラウザを閉じる
browser.quit()

