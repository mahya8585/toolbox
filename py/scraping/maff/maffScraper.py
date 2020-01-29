import requests
from urllib import request
from bs4 import BeautifulSoup
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO


def read_pdf(pdf_url):
    """pdfの読み込み

    :param pdf_url:
    :return:
    """
    # 抽出パラメータ設定
    laparams = LAParams()
    laparams.detect_vertical = True

    # 抽出器の作成
    string_io = StringIO()
    pdf_rm = PDFResourceManager()
    converter = TextConverter(pdf_rm, string_io, codec='utf-8', laparams=laparams)
    interpreter = PDFPageInterpreter(pdf_rm, converter)

    # PDFの読み出し
    # pdf_file = open(pdf_url, 'rb')
    pdf_file = request.urlopen(pdf_url)
    # TODO: 今ここでエラー出てる
    for page in PDFPage.get_pages(pdf_file.read(), set(), maxpages=0, caching=True, check_extractable=True):
        interpreter.process_page(page)
        print(string_io.getvalue())

    pdf_file.close()
    converter.close()
    string_io.close()
    print('#######################')


url = 'https://www.maff.go.jp/j/supply/nyusatu/zuii/rakusatu/index.html'

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
