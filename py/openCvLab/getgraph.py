import cv2
import os
import numpy as np


def display_image(img):
    """
    debug用。画像途中表示
    :param img:
    :return:
    """
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def extract_graph(imread):
    """
    膨張処理
    :param imread:
    :return:
    """
    # グレースケール
    gray = cv2.cvtColor(imread, cv2.COLOR_RGB2GRAY)
    display_image(gray)

    # 二値化
    ret, th1 = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY)
    display_image(gray)

    ret, contours, hierarchy = cv2.findContours(th1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print("検出した輪郭の数：", len(contours), "hierarchy=", len(hierarchy))

    # 抽出した輪郭を描画してみる
    for c in contours:
        cv2.drawContours(imread, c, -1, (0, 255, 0), 3)

    display_image(imread)


if __name__ == '__main__':
    # グラフを数値化してみる処理
    IMAGE_DIR = os.path.abspath(os.path.dirname(__file__)) + '/comparison/'
    # 画像サイズが一緒でない場合は画像サイズを合わせたほうがいい
    # IMAGE_SIZE = (993, 449)

    SOURCE_FILE_NAME = '2.png'
    source = cv2.imread(IMAGE_DIR + SOURCE_FILE_NAME)

    display_image(source)

    extract_graph(source)



