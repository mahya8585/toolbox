import cv2
import numpy as np
import math
import os


def ready_image(file_path):
    """
    openCV読み込み
    :param file_path:
    :param mode:
    :return:
    """
    return cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)


def extract_horizontal(x1, x2, y1, y2, target_imread):
    """
    水平直線のみを取得する
    :param x1:
    :param x2:
    :param y1:
    :param y2:
    :param target_imread:
    :return:
    """
    arg = math.degrees(math.atan2((y2 - y1), (x2 - x1)))
    # 水平値
    HORIZONTAL = 0
    # 許容誤差
    DIFF = 100
    if arg > HORIZONTAL - DIFF and arg < HORIZONTAL + DIFF:
        print('傾き：' + str(arg - HORIZONTAL))
        cv2.line(target_imread, (x1, y1), (x2, y2), (255, 255, 255), 2)

    return target_imread


def extract_houghline(target_imread):
    """
    hough line変換を行う
    :param target_imread: imredd
    :return: 加工済みimread
    """
    # TODO グラフ直線だけを取得するということができていない
    lines = cv2.HoughLines(target_imread, 1, np.pi / 180, 200)
    print('lineカウント：' + str(len(lines)))

    for line in lines:
        rho, theta = line[0]

        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        # 水平直線のみを取得する
        target_imread = extract_horizontal(x1, x2, y1, y2, target_imread)

        # 全ライン取得
        # cv2.line(target_imread, (x1, y1), (x2, y2), (255, 0, 255), 2)

    return target_imread


def write_image(target_imread, output_file_path):
    """
    画像ファイルの書き出し
    :param target_imread: imread
    :param output_file_path: ファイルパス
    :return: なし（画像を吐き出す
    """
    output_dir = os.path.join(os.getcwd(), 'result', output_file_path)
    cv2.imwrite(output_dir, target_imread)


if __name__ == '__main__':
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    target = ready_image(BASE_DIR + '/comparison/1.png')

    # 水平線の抽出
    include_lines = extract_houghline(target)

    write_image(include_lines, BASE_DIR + '/result/straight.png')
