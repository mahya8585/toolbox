import cv2
import os.path
import numpy as np
import math


def ready_use_opencv(image_path):
    """
    opencv利用準備
    :param image_path: 画像パス
    :return: imread
    """
    # 画像入力　第2引数は 1: カラー 0: モノクロ
    return cv2.imread(image_path, 1)


def write_image(target_imread, outputFileName):
    """
    画像ファイルの書き出し
    :param target_imread: imread
    :param outputFileName: ファイル名
    :return: なし（画像を吐き出す
    """
    output_dir = os.path.join(os.getcwd(), 'result', outputFileName)
    cv2.imwrite(output_dir, target_imread)


def cut_image(target_imread):
    """
    画像を切り出す
    :param target_imread: imread
    :return: 加工済みimread
    """
    # 切り出したい場所を代入（2点im[y:y+h, x:x+w]を通る矩形部分を切り抜き）
    return target_imread[100:650, 95:820]


def extract_edges(target_imread, debugged):
    """
    エッジ抽出する
    :param target_imread: imread
    :param: debugged : false:デバッグしない true:デバッグする
    :return: 加工済みimread
    """
    gray_scale = cv2.cvtColor(target_imread, cv2.COLOR_BGR2GRAY)

    # ノイズ直線(補助線とか)を削除する
    _, binary_threshold = cv2.threshold(gray_scale, 120, 255, cv2.THRESH_BINARY)
    edges = cv2.bitwise_not(binary_threshold)
    # edges = cv2.Canny(binary_threshold, 100, 200, apertureSize=7)


    # デバッグ用
    if debugged:
        write_image(binary_threshold, 'binary_threshold.png')
        write_image(edges, 'edge.png')

    return edges


def extract_horizontal(x1, x2, y1, y2, target_imread):
    # 水平直線のみを取得する
    arg = math.degrees(math.atan2((y2 - y1), (x2 - x1)))
    # 水平値
    HORIZONTAL = 0
    # 許容誤差
    DIFF = 10
    if arg > HORIZONTAL - DIFF and arg < HORIZONTAL + DIFF:
        print('傾き：' + str(arg - HORIZONTAL))
        cv2.line(target_imread, (x1, y1), (x2, y2), (255, 0, 255), 2)

    return target_imread


def extract_vertical(x1, x2, y1, y2, target_imread):
    # 垂直線のみを取得する
    arg = math.degrees(math.atan2((y2 - y1), (x2 - x1)))
    # 垂直の値
    VERTICAL = 90
    # 許容誤差
    DIFF = 1
    if arg > VERTICAL - DIFF or arg < - (VERTICAL - DIFF):
        print('傾き：' + str(arg - VERTICAL))
        cv2.line(target_imread, (x1, y1), (x2, y2), (255, 0, 255), 2)

    return target_imread


def write_houghline(target_imread):
    """
    hough line変換を行う
    :param target_imread: imredd
    :return: 加工済みimread
    """
    # TODO グラフ直線だけを取得するということができていない
    lines = cv2.HoughLines(extract_edges(target_imread, True), 1, np.pi / 180, 200)
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
        # target_imread = extract_horizontal(x1, x2, y1, y2, target_imread)]
        # 垂直線のみを取得する
        extract_vertical(x1, x2, y1, y2, target_imread)
        # 全ライン取得
        # cv2.line(target_imread, (x1, y1), (x2, y2), (255, 0, 255), 2)

    return target_imread


def write_houghline_p(target_imread):
    """
    確率的hough line変換を行う
    :param target_imread: imredd
    :return: 加工済みimread
    """
    minLineLength = 200
    maxLineGap = 30

    lines = cv2.HoughLinesP(extract_edges(target_imread, True),
                            1, np.pi / 180, 100, minLineLength, maxLineGap)
    print('lineカウント：' + str(len(lines)))

    for line in lines:
        x1, y1, x2, y2 = line[0]

        # 水平直線のみを取得する
        # target_imread = extract_horizontal(x1, x2, y1, y2, target_imread)
        # 垂直線のみを取得する
        #extract_vertical(x1, x2, y1, y2, target_imread)
        # 全ライン取得
        cv2.line(target_imread, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return target_imread


if __name__ == '__main__':
    # 共通準備処理
    target_imread = ready_use_opencv('sample.png')

    # 画像切り出し
    # write_image(cut_image(target_imread), 'cut.png')

    # houghline書き込み
    write_image(write_houghline(target_imread), 'houghline.png')

    # 確率的hough line 書き込み
    # write_image(write_houghline_p(target_imread), 'houghlineP.png')
