# pyminerを使用して指定したPDFファイルからテキストを抽出する
import os
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFPageInterpreter
from io import StringIO

# ファイルパス
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PDF_PATH = os.path.join(BASE_DIR, 'mojibake.pdf')

# PDFファイルを読み込む
fp = open(PDF_PATH, 'rb')
outIO = StringIO()
rmgr = PDFResourceManager()

txtcvt = TextConverter(rmgr, outIO, laparams=LAParams())
iprtr = PDFPageInterpreter(rmgr, txtcvt)

# PDFファイルから1ページずつ解析(テキスト抽出)処理する
for page in PDFPage.get_pages(fp, maxpages=3):
    iprtr.process_page(page)
    print(outIO.getvalue())
    print('------------------------')

outIO.close()
txtcvt.close()
fp.close()
