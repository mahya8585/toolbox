from pathlib import Path
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv


def extract_station_urls(top_page):
    """取得する&書き出し
    :param top_page: htmlテキストデータ
    """
    # とりあえずhtml_parserで回すよー
    page_soup = BeautifulSoup(top_page, 'html.parser')

    train_lines = page_soup.find_all('div', class_='trainLine')

    # key: 路線名 value: 駅情報(辞書型)
    line_stations = {}
    for train_line in train_lines:
        line_name = train_line.find('span', class_='name').text

        # key: 駅名 value: 詳細ページURL
        stations = {}
        stations_info = train_line.find_all('a')
        for station_info in stations_info:
            station_url = station_info['href']
            station_name = station_info.find('span').text.strip()
            stations[station_name] = station_url

        line_stations[line_name] = stations

    return line_stations


def extract_poster_place(st_page):
    """取得する&書き出し
    :param st_page: htmlテキストデータ
    """
    # とりあえずhtml_parserで回すよー
    page_soup = BeautifulSoup(st_page, 'html.parser')

    poster_place = page_soup.find('p', class_='txtCenter').find('span').text

    return poster_place.replace('・', '').strip()


def extract_inout(place):
    inside = "改札内"
    outside = "改札外"

    inout = ""

    if inside in place:
        inout = inside

    if outside in place:
        if inout != "":
            inout = inout + ","

        inout = inout + outside

    return inout


def create_poster_place_csv():
    """WEBサイトログインし、駅のポスター情報を取得する。CSVに吐き出す。
    """
    csv_result = Path.cwd().joinpath('poster-place.csv')
    site_domain = 'https://www.event-metro.jp'
    email = 'ログインメール'
    password = 'ログインパスワード'

    # web driver発動(Chrome102対応中です。バージョンは都度確認してください)
    driver = webdriver.Chrome(executable_path=Path.cwd().joinpath('chromedriver'))
    driver.get(site_domain + '/rally/all-stations/login/')

    # ログイン処理
    driver.find_element(By.ID, 'email').send_keys(email)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.NAME, 'submit').click()

    with open(csv_result, 'w') as f:
        writer = csv.writer(f)

        for l_name, st_info in line_station_urls.items():
            # 駅ポスター情報取得
            for st_name, st_url in st_info.items():
                print(site_domain + st_url)
                time.sleep(1)

                # (サイトバグ対応)
                driver.get(site_domain + st_url.replace('checked', 'detail'))
                place_text = extract_poster_place(driver.page_source)

                # 改札内外情報
                inout_text = extract_inout(place_text)

                writer.writerow([l_name, st_name, place_text, inout_text, site_domain + st_url])
                # マッピング用
                # writer.writerow([l_name, st_name + "駅", place_text, inout_text, site_domain + st_url])

    driver.close()


# メイン処理ここから
"""東京メトロ全駅スタンプラリーのサイトhtmlもってきました。
"""
html_main = Path.cwd().joinpath('target.html')

# メインページ情報(静的ファイル)から路線名・駅名・駅詳細ページURL取得
with open(html_main, 'r', encoding='utf8') as hf:
    line_station_urls = extract_station_urls(hf.read())

# WEBページにログインし、スタンプラリー情報を取得し、CSV化する
create_poster_place_csv()

print('function end.')
