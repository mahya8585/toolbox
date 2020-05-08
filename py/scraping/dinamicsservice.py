import requests
import re
from bs4 import BeautifulSoup


def extract_name(web_page):
    """メニューから機能一覧を取得する
    :param web_page: request.textデータ
    """
    # とりあえずhtml_parserで回すよー
    page_soup = BeautifulSoup(web_page.text, 'html.parser')
    applications = page_soup.find_all('div', class_='c-uhf-menu js-nav-menu')

    # 英語のみを抽出するためのregex
    p = re.compile('[a-zA-Z0-9]+')

    for application in applications:
        app_button = application.find('button')

        if app_button.text == 'アプリケーション':
            services = application.find_all('li',  class_='f-sub-menu js-nav-menu')

            for service in services:
                service_button = service.find('button')
                # サービス名
                service_name = service_button.text

                # 機能名（英語のみを抽出)
                functions = service.find_all('a', class_='js-subm-uhf-nav-link')
                blank = True
                for function in functions:
                    if p.fullmatch(function.text.replace(' ', '')):
                        print(service_name + ' : ' + function.text)
                        blank = False

                # 機能名がないものはサービス名のみ記載
                if blank:
                    print(service_name)

            break


# メイン処理ここから
url = requests.get('https://dynamics.microsoft.com/ja-jp/')

# サービス名だけ(重複排除済み・プレビュー込み)
extract_name(url)


print('function end.')
