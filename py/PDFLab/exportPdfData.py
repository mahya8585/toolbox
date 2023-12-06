# pypdfを使用して指定したPDFファイルからテキストを抽出する
import os
import chardet
from pypdf import PdfReader

# ファイルパス
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PDF_PATH = os.path.join(BASE_DIR, 'mojibake.pdf')
# PDF_PATH = os.path.join(BASE_DIR, 'correct.pdf')

# PDFファイルを読み込む
pdf = PdfReader(PDF_PATH)

# ページ数を取得する
pages = len(pdf.pages)

# ページ数分のテキストを抽出する
for i in range(pages):
    page = pdf.pages[i]
    text = page.extract_text()

    # # 文字コードを判定する
    encode = chardet.detect(text.encode())['encoding']
    print(encode)

    # テキストの出力
    print(text)
    print('------------------------')

print('PDFファイルのページ数: ', pages)
