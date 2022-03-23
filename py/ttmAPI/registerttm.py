import pandas as pd
import requests
import io
import datetime
import redis

"""みずほのサイトからデータを取得し、DBに登録する
:param year: 登録したい年
"""
# みずほのサイトからデータを取得
FILE_PATH = 'https://www.mizuhobank.co.jp/market/csv/quote.csv'
csv_file = requests.get(FILE_PATH)

# 日付とドルデータのみ抽出&便宜上表頭付与
last_year = str(datetime.datetime.now().year - 1)
df = pd.read_csv(io.BytesIO(csv_file.content), sep=',', encoding='shift-jis')
usd_ttms = df.iloc[:, [0, 1]].dropna(axis=0).rename(columns={'Unnamed: 0': 'date', 'Unnamed: 1': 'usd'})

# redis設定(既存データの削除をふくむ)
redis_server = redis.Redis(
    host='さーばほすと',
    port=6380,
    password='ぱすわーど',
    ssl=True
)
redis_server.flushdb()

# 日付が去年のデータをredisに登録
for row in usd_ttms.itertuples():
    date_split = row.date.split('/')

    if date_split[0] == last_year:
        # keyからyearを削除、およびMMdd型に変更
        redis_server.set(date_split[1]+date_split[2], row.usd)

print('function end.')
