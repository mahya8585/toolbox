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


def judge_4points(coordinate, img_height, img_weight):
    """
    画像の角にある輪郭点は対象外とする
    :param contours: 輪郭点list
    :param img_height: 画像の高さ
    :param img_weight: 画像の幅
    :return: true: 角付近の座標 false: それ以外
    """
    # 四つ角判定変数
    p = 3

    x = coordinate[0][0]
    y = coordinate[0][1]

    is_x_end = False
    if x <= p or img_weight - p <= x:
        is_x_end = True

    is_y_end = False
    if y <= p or img_height - p <= y:
        is_y_end = True

    # xもyも両端であった場合、四つ角である
    if is_x_end and is_y_end:
        return True

    return False


def extract_graph(imread, img_height, img_weight):
    """
    膨張処理
    :param imread:
    :param img_height:
    :param img_weight:
    :return:
    """
    # 二値化
    gray = cv2.cvtColor(imread, cv2.COLOR_RGB2GRAY)
    ret, th1 = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY)

    # 輪郭抽出
    ret, contours, hierarchy = cv2.findContours(th1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(imread, contours, -1, (0, 255, 0), 3)
    # display_image(imread)

    # 抽出した輪郭から必要な情報だけを抽出
    all_array = []
    for contour in contours:
        for c in contour:
            # 四辺の輪郭点は対象外とする
            if not judge_4points(coordinate=c, img_height=img_height, img_weight=img_weight):
                all_array.append(c[0])

    return all_array


def complement_value(coordinates, x_size):
    """
    グラフ数値補完・削除処理
    :param coordinates: 座標データ
    :param x_size:
    :return:
    """
    # X座標準にソート
    coordinates.sort(key=lambda x: (x[0], x[1]))

    # x軸に対応するyデータを整形する
    complements = []
    for x in range(x_size):
        correct = []
        is_continue = True

        # xの値が同値の場合はｙの値が大きいほうを採用する = あとから入ってきたデータを採用する
        # TODO グラフが下に下がることを考慮してなかったので後程直す
        while is_continue:
            if len(coordinates) <= 0:
                if 0 < len(correct):
                    insert_data = [correct[0], correct[1]]
                else:
                    insert_data = [x, complements[len(complements) - 1][1]]

                complements.append(insert_data)
                break

            target = coordinates.pop(0)
            if target[0] == x:
                correct = target
                continue
            else:
                # 対象のx軸データが存在する場合は左記データを採用
                if 0 < len(correct):
                    append_data = [correct[0], correct[1]]

                else:
                    # 元データが存在しない場合は1つ前に採用されたデータと同じyの値を設定する
                    if 0 < len(complements):
                        append_data = [x, complements[len(complements) - 1][1]]

                    # 前に採用されたデータ存在しない場合は後続のデータと同じ値を設定する
                    else:
                        append_data = [x, coordinates[0][1]]

                complements.append(append_data)
                # popしてしまったデータを元に戻す
                coordinates.insert(0, target)
                is_continue = False

    return complements


def split_coodinates(coordinates, split_count):
    """
    座標データを分割する
    :param coordinates: 座標データ(x軸すべてに値が補完されていること)
    :param split_count: 分割数
    :return: 分割データリスト
    """
    split_point = len(coordinates) // split_count
    response = []

    # 指定した数ずつに分割したデータリストを作成
    start = 0
    while len(coordinates) - start >= split_point:
        response.append(coordinates[start:start + split_point])
        start = start + split_point

    # 剰余データの処理
    response.append(coordinates[start:])

    return response


def create_coordinates_list(img, split_count):
    """
    座標データを指定した数＋1に分割したリストを作成する
    :return: 分割済み座標セット
    """
    # 輪郭抽出（グラフ点抽出)
    img_height, img_weight = img.shape[:2]
    coordinates = extract_graph(imread=img, img_weight=img_weight, img_height=img_height)

    # 抽出したエッジ内のスパースな部分を補完する
    graph_coordinates = complement_value(coordinates=coordinates, x_size=img_weight)

    # データセット分割
    return split_coodinates(graph_coordinates, split_count)


def compare(source_coordinates, target_coordinates):
    """
    分割したファイルをそれぞれ比較し、類似度を確認する
    :param source_coordinates:
    :param target_coordinates:
    :return:
    """
    print("類似度判定を行います。数値が小さいほど類似しています")
    for list_index in range(SPLIT_CNT):
        s_coordinates = source_coordinates[list_index]
        t_coordinates = target_coordinates[list_index]

        distances = []
        for array_index in range(len(s_coordinates)):
            sc = np.array(s_coordinates[array_index])
            tc = np.array(t_coordinates[array_index])

            distances.append(np.linalg.norm(sc - tc))

        similar = sum(distances) / len(distances)
        print(str(list_index + 1) + '枚目の画像の類似度：' + str(similar))


if __name__ == '__main__':
    # グラフを数値化してみる処理
    IMAGE_DIR = os.path.abspath(os.path.dirname(__file__)) + '/comparison/'
    # 画像サイズが一緒でない場合は画像サイズを合わせたほうがいい
    # IMAGE_SIZE = (993, 449)

    # 画像分割数
    SPLIT_CNT = 5

    # 評価元画像
    source = cv2.imread(IMAGE_DIR + '1.png')
    source_coordinates = create_coordinates_list(source, SPLIT_CNT)

    # 評価対象画像
    target = cv2.imread(IMAGE_DIR + '2.png')
    target_coordinates = create_coordinates_list(target, SPLIT_CNT)

    # TODO マッチングして類似か判定するぞ(for文で) 総和の平均とかでまずは算出
    compared = compare(source_coordinates, target_coordinates)
