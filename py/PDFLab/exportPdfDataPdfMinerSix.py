# PdfMiner.sixを使用して指定したPDFファイルからテキストを抽出する
import os
from pdfminer.high_level import extract_text

# ファイルパス
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PDF_PATH = os.path.join(BASE_DIR, 'mojibake.pdf')
# PDF_PATH = os.path.join(BASE_DIR, 'correct.pdf')

# テキストを抽出する
text = extract_text(PDF_PATH)

# テキストの出力
print(text)
print('------------------------')

