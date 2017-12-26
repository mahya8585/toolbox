import cv2
import os

# 複数枚比較するよー
# 同じサイズの画像を比較する前提なので画像リサイズ処理は省くよー

IMAGE_DIR = os.path.abspath(os.path.dirname(__file__)) + '/comparison/'

# 特徴量抽出処理の選定
detector = cv2.ORB_create()

# 比較元の特徴量抽出(今回はグレースケールでの抽出とする)
SOURCE_FILE_NAME = '1.png'
source = cv2.imread(IMAGE_DIR + SOURCE_FILE_NAME, cv2.IMREAD_GRAYSCALE)

(source_kp, source_des) = detector.detectAndCompute(source, None)

# 画像ディレクトリ内のファイルをすべて比較し、一番類似度の高いものを決定する
first_prize = {
    'name': '',
    'similarity': 0
}
matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
images = os.listdir(IMAGE_DIR)
for image in images:
    if image == SOURCE_FILE_NAME or image == '__init__.py':
        continue

    # 比較対象の設定
    target = cv2.imread(IMAGE_DIR + image, cv2.IMREAD_GRAYSCALE)
    (target_kp, target_des) = detector.detectAndCompute(target, None)

    # 類似度確認
    matches = matcher.match(target_des, source_des)
    matches = sorted(matches, key=lambda x: x.distance)

    dist = [m.distance for m in matches]
    ret = sum(dist) / len(dist)

    # 距離を算出しているので、数値が小さいほど類似度が高いといえる
    # print(dist)
    print(image + ' ：' + str(ret))

    if first_prize['name'] == '' or first_prize['similarity'] > ret:
        first_prize['name'] = image
        first_prize['similarity'] = ret

print('一番類似しているグラフは' + first_prize['name'] + 'で、' + str(first_prize['similarity']) + 'でした。')