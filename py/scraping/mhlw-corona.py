import requests
from bs4 import BeautifulSoup
import pandas as pd

# 厚労省のコロナページへアクセス
mhlw_page = requests.get('https://www.mhlw.go.jp/stf/newpage_11178.html')
mhlw_page.encoding = mhlw_page.apparent_encoding

# 世界のコロナ罹患者情報をスクレイピング
page_soup = BeautifulSoup(mhlw_page.text, 'html.parser')
world_corona_info = page_soup.find_all('div', class_='m-grid__col1')
world_corona = world_corona_info[0].find_all('tr')

import_data = []
for line in world_corona:
    worlds = line.find_all('td')
    if len(worlds) == 3:
        corona_positive = worlds[1].text.replace(',', '')
        die = worlds[2].text.replace(',', '')
        import_data.append([worlds[0].text, corona_positive, die])
    else:
        continue

# dataflame化
import_data.pop(0)
import_data.pop(-1)
world_corona_positive = pd.DataFrame(import_data, columns=['country', 'corona-positive', 'die'], dtype=int)

