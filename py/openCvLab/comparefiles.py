import cv2
import os

# 複数枚比較するよー
# 同じサイズの画像を比較する前提なので画像リサイズ処理は省くよー

def read_gray(file_path):
    """
    openCV読み込み(グレースケール)
    :param file_path:
    :param mode:
    :return:
    """
    return cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

def detect_features(cv_image):
    """
    特徴量の検出
    :param cv_image:
    :return:
    """
    # 特徴量抽出処理の選定
    detector = cv2.ORB_create()
    return detector.detectAndCompute(cv_image, None)

def extract_matches(target_des, source_des):
    """
    類似度検出
    :param target_des:
    :param source_des:
    :return:
    """
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
    matches = matcher.match(target_des, source_des)

    return sorted(matches, key=lambda x: x.distance)

def compare_images(target_dir, source_name, source_des):
    """
    対象ファイル群の中から比較元画像に一番類似している画像を検出する
    :param target_dir:
    :param source_name:
    :param source_des:
    :return:
    """
    first_prize = {
        'name': '',
        'similarity': 0
    }

    for image in os.listdir(target_dir):
        if image == source_name or image == '__init__.py':
            continue

        # 比較対象の設定
        (target_kp, target_des) = detect_features(read_gray(target_dir + image))

        # 類似度確認
        dist = [m.distance for m in extract_matches(target_des, source_des)]
        ret = sum(dist) / len(dist)

        # 距離を算出しているので、数値が小さいほど類似度が高いといえる
        print(image + ' ：' + str(ret))
        if first_prize['name'] == '' or first_prize['similarity'] > ret:
            first_prize['name'] = image
            first_prize['similarity'] = ret

    return first_prize


if __name__ == '__main__':
    IMAGE_DIR = os.path.abspath(os.path.dirname(__file__)) + '/comparison/'

    # 比較元の特徴量抽出(今回はグレースケールでの抽出とする)
    SOURCE_FILE_NAME = '1.png'
    (source_kp, source_des) = detect_features(read_gray(IMAGE_DIR + SOURCE_FILE_NAME))

    # 画像ディレクトリ内のファイルをすべて比較し、一番類似度の高いものを決定する
    first_prize = compare_images(IMAGE_DIR, SOURCE_FILE_NAME, source_des)

    print('一番類似しているグラフは' + first_prize['name'] + 'で、' + str(first_prize['similarity']) + 'でした。')