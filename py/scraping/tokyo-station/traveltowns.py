import requests
from bs4 import BeautifulSoup
import redis


def scraping_tokyo_stations(html: str):
    """東京の駅一覧を取得する

    Args:
        html (str): 東京の駅一覧が表示されてるサイトのHTML

    Returns:
        list: 駅名のリスト
    """
    soup = BeautifulSoup(html, 'html.parser')
    stations_table = soup.find(id='main').find('table').find_all('tr')

    # 1行目は表頭なので削除、2行目から駅名を取得
    return [station.find('td').find('a').text for station in stations_table[1:]]


def exist_hashi(stations: list):
    """"橋"の字を含む駅名を抽出する

    Args:
        stations (list): 駅名のリスト

    Returns:
        list: "橋"の字を含む駅名のリスト
    """
    return [station for station in stations if '橋' in station]


def create_stations_db(stations: list):
    """駅名のリストをKVSに保存する

    Args:
        stations (list): 駅名のリスト
    """
    # Azure cache for Redis に接続
    conn = redis.StrictRedis(
        host='HOST_NAME',
        port=6380,
        db=0,
        password='ACCESS_KEY',
        ssl=True
    )

    # 駅名をKVSに保存
    for station_name in stations:
        conn.set(station_name, '')


# メイン処理ここから
"""トラベルタウンの東京の駅一覧を取得する
"""
html_tokyo_stations = requests.get('https://www.traveltowns.jp/eki/tokyo/').text


# 駅名一覧の作成
tokyo_stations = scraping_tokyo_stations(html_tokyo_stations)

# "橋"の字を含む駅名を抽出
target_tokyo_stations = exist_hashi(tokyo_stations)

# 駅KVSの作成
create_stations_db(target_tokyo_stations)

print('end.')
