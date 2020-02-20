import requests
import time
from bs4 import BeautifulSoup


def read_pdf(pdf_url):
    """pdfの読み込み

    :param pdf_url:
    :return:
    """
    # TODO scraper.pyで検証完了したコードをここにぶっこむ


url = 'https://.maff.go.jp/j/supply/nyusatu/zuii/rakusatu/index.html'

# pdfの取得
content = requests.get(url)

# pdf情報のある場所を取得
base_soup = BeautifulSoup(content.text, 'html.parser')
pdf_contents = base_soup.find(attrs={'id': 'main_content'}).find('ul').find_all('li')

# pdfパスの作成
html_delete = url.split('/')[-1]
url_path = url.rstrip(html_delete)

for pdf_content in pdf_contents:
    # TODO: newアイコンがついてるものだけ取得して処理するというフェーズをfunction化したときに追加する
    # リンク情報の取得
    target_url = url_path + pdf_content.a.get('href').lstrip('./')

    # pdf 情報の取得と書き出し
    read_pdf(target_url)
    time.sleep(2)
    break

print('exit.')
