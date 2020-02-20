import sys
from pathlib import Path
from subprocess import call


pdf_url = 'index-36.pdf'
output = 'extract-pdf.txt'

# TODO 今ファイルをここで作ってしまってるので後続処理でエラーになります。一番下にあるtikaでやりたい、
pdf2txt_path = Path(sys.exec_prefix) / 'Scripts' / 'pdf2txt.py'
call(['py', str(pdf2txt_path), '-o ' + output, '-p 1', pdf_url])

print('#######################')

with open(output, 'r', encoding='utf-8') as f:
    lines = [s.strip() for s in f.readlines()]

    count = 0
    result = ''
    for line in lines:
        if count > 0:
            if '①' in line:
                count = 2
                result = line
            elif count > 1:
                result = result + ' ' + line
            else:
                print('skip')
        else:
            if '①' in line:
                # 1つめの情報は説明文であるため保持しない
                count = 1

    print(result)

# from tika import parser
# 本当はこっちでやりたい tika-pythonのバージョンバグ踏み中。アップデート待ち
#
# file_data = parser.from_file('index-36.pdf')
# extract_text = file_data['content']
# print(extract_text)



