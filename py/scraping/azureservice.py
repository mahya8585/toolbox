import requests
from bs4 import BeautifulSoup


def extract_name(web_page):
    """取得する
    :param web_page: request.textデータ
    """
    # とりあえずhtml_parserで回すよー
    page_soup = BeautifulSoup(web_page.text, 'html.parser')
    azure_services = page_soup.select('h3[class="h5"]')

    service_names = []
    for service_obj in azure_services:
        service_name_link = service_obj.find('a')
        service_name = service_name_link.find('span')
        result_name = service_name.text.replace('ᴾᴿᴱⱽᴵᴱᵂ', '')
        service_names.append(result_name)

    print('全サービス数 : ' + str(len(service_names)))
    name_set = dict.fromkeys(service_names)
    print('重複排除 : ' + str(len(name_set)))
    for key in name_set:
        print(key)


def extract_category_name(web_page):
    """重複アリ・カテゴリと名前のセットを取得する
    :param web_page: request.textデータ
    """
    # とりあえずhtml_parserで回すよー
    page_soup = BeautifulSoup(web_page.text, 'html.parser')
    contents = page_soup.find(id='products-list')
    h2s = contents.find_all('h3')

    category = ''
    for h2 in h2s:
        line = h2.find('span')

        if line is None:
            category = h2.text
            continue
        else:
            print(category + ',' + line.text)


# メイン処理ここから
url = requests.get('https://azure.microsoft.com/ja-jp/services/')

# サービス名だけ(重複排除済み・プレビュー込み)
extract_name(url)
# カテゴリ・サービス名の対応一覧(サービス重複のまま)
# extract_category_name(url)


print('function end.')
