# -*- coding: utf-8 -*-
from PIL import Image
import os
import shutil


def save_img(image_dir, file_name, result_dir):
    """
    二値化画像の保存をおこなう
    :param image_dir: イメージディレクトリパス
    :param file_name: ファイル名
    :param result_dir: 結果ファイル保存ディレクトリパス
    """
    # 二値化する(グレースケールにしてから)
    target = Image.open(image_dir + file_name)
    gray_target = target.convert('L')
    new_image = gray_target.point(judge_binary)

    # ファイル保存
    new_image.save(result_dir + file_name)


def judge_binary(col):
    """
    二値化処理
    :param col: 対象点の明度数値
    :return:二値化数値
    """
    threshold = 80

    if col > threshold:
        return 255
    else:
        return 0


def make_img_name_list(image_dir):
    """
    ディレクトリ内に存在するファイルの名前一覧を取得する
    :param image_dir: 対象ディレクトリパス
    :return: ファイル名リスト
    """
    # TODO 拡張子チェックを行っていません。チェック処理を追加するべき・・・

    return os.listdir(image_dir)


def main():
    # TODO 画像操作対象ディレクトリパス
    image_dir = './image//'

    # 保存ディレクトリの削除
    result_dir = image_dir + 'result//'
    if os.path.isdir(result_dir):
        shutil.rmtree(result_dir)

    # ファイル名一覧の取得
    img_names = make_img_name_list(image_dir)

    # 結果保存ディレクトリの作成
    os.mkdir(result_dir)

    # ディレクトリ内すべてのファイルを二値化変換
    for img_name in img_names:
        print('start : ' + img_name)
        save_img(image_dir, img_name, result_dir)


if __name__ == "__main__":
    main()
