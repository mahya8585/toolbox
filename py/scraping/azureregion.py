import requests
from bs4 import BeautifulSoup


def extract_area(web_page):
    """取得する
    :param web_page: request.textデータ
    """
    # とりあえずhtml_parserで回すよー
    page_soup = BeautifulSoup(web_page.text, 'html.parser')
    target = page_soup.find('div', class_='row row-size3 column')
    azure_area_body = target.find('p', class_='text-body5')

    areas = azure_area_body.text.split(sep='。')[1].split(sep='、')

    print('エリア数 : ' + str(len(areas)))
    print(areas)
    print(azure_area_body.text)


def extract_region(web_page):
    """重複アリ・カテゴリと名前のセットを取得する
    :param web_page: request.textデータ
    """
    # とりあえずhtml_parserで回すよー
    page_soup = BeautifulSoup(web_page.text, 'html.parser')
    target = page_soup.find(id='new-regions').find('div', class_='row row-size2 column')
    azure_region_body = target.find('p', class_='text-body5')

    regions = azure_region_body.text.split(sep='。')[1].split(sep='、')

    print('リージョン数 : ' + str(len(regions)))
    print(regions)
    print(azure_region_body.text)


# メイン処理ここから
url = requests.get('https://azure.microsoft.com/ja-jp/global-infrastructure/geographies/')

# 地域
extract_area(url)
# リージョン
extract_region(url)



print('function end.')
