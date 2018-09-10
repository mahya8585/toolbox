"""
1. connpass参加者CSVから登壇者枠を抽出する
2. タイトルと登壇者名を抽出し、スピーカー辞書を作る
3. ランダムに取り出して発表順番を決定
"""
import csv
import random


def create_speakers(file_name):
    """
    スピーカ辞書の作成
    :param file_name:ファイル名またはファイルパス。名前だけの場合は同ディレクトリ内に対象ファイルがあると想定して動きます。
    :return:辞書型スピーカー情報 key:name value:title
    """
    # 抽出枠名 カラム名,枠名
    category = [0, 'LT枠(男女問わず) All Gender']
    # 名前カラム番号
    name = 2
    # タイトルカラム番号
    title = 10

    csv_file = open(file_name, 'r', encoding='ms932', errors='', newline='')
    members = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"')

    # スピーカー情報の抽出
    speakers = {}
    for member in members:
        if member[category[0]] == category[1]:
            speakers.update({member[name]: member[title]})

    return speakers


def draw_for_turns(speakers):
    """
    ランダムに順番決めるよー
    :param speakers: key:スピーカー名 value: タイトル
    :return:
    """
    keys = list(speakers.keys())
    random.shuffle(keys)

    for key in keys:
        print('名前：{} , タイトル: {}'.format(key, speakers[key]))


if __name__ == '__main__':
    # ファイル名またはファイルパス
    # とりあえずconnpassから取得できるファイルフォーマットを想定しています(encode: ms932 , 改行：CRLF)。
    file_path = 'event.csv'

    # スピーカー辞書作成
    speakers_dict = create_speakers(file_path)

    # 発表順決定
    draw_for_turns(speakers_dict)
