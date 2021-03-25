from bs4 import BeautifulSoup
from pathlib import Path
import csv


def extract_info(web_page):
    """取得する&書き出し
    :param web_page: htmlテキストデータ
    """
    # とりあえずhtml_parserで回すよー
    page_soup = BeautifulSoup(web_page, 'html.parser')
    founds = page_soup.find_all('li', class_='card')

    for found in founds:
        name = found.find('h2', class_='holdfund-title')
        investment = found.find('div', class_='holdfund-amount').find('div', class_='holdfund-txt')
        allocation = found.find('div', class_='holdfund-allocation').find('div', class_='holdfund-txt')
        status = found.find('div', class_='holdfund-status')
        profits = found.find('div', class_='holdfund-yield').find('div', class_='holdfund-txt')

        write_list = [
            name.text,
            investment.text.replace('¥', ''),
            allocation.text.replace('¥', ''),
            status.text.strip(),
            profits.text.replace('%', '').strip()
            ]
        print('\t'.join(write_list))


# メイン処理ここから
"""cloudクレジットの保有ファンド一覧から欲しい情報をとってくる。TSV化する。その後は良しなに。
注：認証処理が面倒だったのでとりあえず第一陣開発ではローカルにhtmlファイルをダウンロードしてあるところから進めます
mypage/investmentrecord/all
F12 + copy outerHTML
"""
html_file = Path.cwd().joinpath('target.html')

with open(html_file, 'r', encoding='utf8') as hf:
    extract_info(hf.read())

print('function end.')
