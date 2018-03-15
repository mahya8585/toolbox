import cv2
import os
import numpy as np

"""
指定カラー抽出
"""


def display_image(img):
    """
    debug用。画像途中表示
    :param img:
    :return:
    """
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def extract(img):
    """
    指定色抽出
    :param img:
    :return:
    """
    # 試しに白背景から緑色を抽出する閾値を設定
    lower = np.array([0, 0, 0])
    upper = np.array([60, 255, 255])

    mask = cv2.inRange(img, lower, upper)
    color_extract = cv2.bitwise_not(mask)

    #todo debug
    display_image(color_extract)

    return color_extract


def complement(imread):
    """
    収縮/膨張処理
    :param imread: 画像データ
    :return:
    """
    # 近傍定義
    # 一般的には4近傍もしくは8近傍を利用するべき
    neighborhood = np.array([[0, 1, 0],
                           [0, 1, 0],
                           [0, 1, 0]],
                          np.uint8)

    erosion = cv2.erode(imread, neighborhood, iterations=2)

    dilation = cv2.dilate(erosion, neighborhood, iterations=2)
    # todo debug
    display_image(dilation)

    return dilation



if __name__ == '__main__':
    IMAGE_DIR = os.path.abspath(os.path.dirname(__file__)) + '/image/'

    target = cv2.imread(IMAGE_DIR + 'target.png')
    trim = extract(target)
    complement = complement(trim)

    # ファイルの書き出し
    cv2.imwrite(IMAGE_DIR + 'complement.png', complement)
