import requests
from bs4 import BeautifulSoup
import time


def extract_url(web_page):
    """ファイルを取得する
    :param web_page: request.textデータ
    """
    # とりあえずhtml_parserで回すよー
    page_soup = BeautifulSoup(web_page.text, 'html.parser')
    answers = page_soup.find_all('div', class_='faq-answers')

    for dev_answer in answers:
        file_devs = dev_answer.find_all('a')

        for file_dev in file_devs:
            # 高負荷にならないようスリープ処理
            time.sleep(3)

            file_url = file_dev.get('href')
            file_name = file_url.split("/")[-1]
            print(file_url)

            response_file = requests.get(file_url)
            if response_file.status_code == 200:
                f = open(file_name, 'w')
                f.write(response_file.content)
                f.close()


# メイン処理ここから
# adventarの取得
url = 'https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page'
extract_url(requests.get(url))


print('function end.')
