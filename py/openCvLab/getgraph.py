import cv2
import os


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
    # TODO


if __name__ == '__main__':
    # グラフを数値化してみる処理
    IMAGE_DIR = os.path.abspath(os.path.dirname(__file__)) + '/comparison/'
    # 画像サイズが一緒でない場合は画像サイズを合わせたほうがいい
    # IMAGE_SIZE = (993, 449)

    SOURCE_FILE_NAME = '1-8avetmp.png'
    source = cv2.imread(IMAGE_DIR + SOURCE_FILE_NAME)
    # display_image(source)

    # 輪郭抽出（グラフ点抽出)
    img_height, img_weight = source.shape[:2]
    coordinates = extract_graph(imread=source, img_weight=img_weight, img_height=img_height)

    # 抽出したエッジ内のスパースな部分を補完する
    graph_coordinates = complement_value(coordinates=coordinates, x_size=img_weight)

    # データセット分割
    split_graph = split_coodinates(graph_coordinates, 5)

    # TODO ターゲットについても↑と同じ情報を取得する

    # TODO 同じエッジ数になったか確認する

    # TODO マッチングして類似か判定するぞ(for文で) 総和の平均とかでまずは算出
