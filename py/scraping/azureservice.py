import requests
from bs4 import BeautifulSoup


def extract_name(web_page):
    """取得する
    :param web_page: request.textデータ
    """
    # とりあえずhtml_parserで回すよー
    page_soup = BeautifulSoup(web_page.text, 'html.parser')
    azure_services = page_soup.find_all('h2', class_='text-heading4')

    service_names = []
    for service_obj in azure_services:
        service_name = service_obj.find('span')
        result_name = service_name.text.replace('プレビュー', '')
        service_names.append(result_name)

    print(len(service_names))
    name_set = dict.fromkeys(service_names)
    print(len(name_set))
    for key in name_set:
        print(key)


# メイン処理ここから
url = 'https://azure.microsoft.com/ja-jp/services/'
extract_name(requests.get(url))

print('function end.')
