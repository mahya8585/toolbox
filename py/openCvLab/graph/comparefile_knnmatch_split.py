import cv2
import os

# 画像を比較して類似度を得る処理

# 特徴量抽出処理の選定
detector = cv2.ORB_create()

IMAGE_DIR = os.path.abspath(os.path.dirname(__file__)) + '/comparison/'
# 画像サイズが一緒でない場合は画像サイズを合わせたほうがいい
# IMAGE_SIZE = (993, 449)

# 画像の分割数
SPLIT_COUNT = 4

# 比較元画像
SOURCE_FILE_NAME = '1.png'
source = cv2.imread(IMAGE_DIR + SOURCE_FILE_NAME)

# 比較対象
TARGET_FILE_NAME = '5.png'
target = cv2.imread(IMAGE_DIR + TARGET_FILE_NAME)

# 画像を分割し、特徴量比較を行う
height, width, channels = source.shape
new_width = int(width / SPLIT_COUNT)
ratio = []
for w in range(SPLIT_COUNT):
    width_start = w * new_width
    width_end = width_start + new_width

    source_clp = source[0:height, width_start:width_end]
    target_clp = target[0:height, width_start:width_end]

    # 特徴量抽出
    (source_kp, source_des) = detector.detectAndCompute(source_clp, None)
    (target_kp, target_des) = detector.detectAndCompute(target_clp, None)

    # 類似度確認
    matches = cv2.BFMatcher(cv2.NORM_HAMMING).knnMatch(source_des, target_des, k=5)

    similar = []
    for m in matches:
        distances = [info.distance for info in m]
        m_rat = sum(distances) / len(m)
        similar.append(m_rat)

    # 画像表示確認
    output = cv2.drawMatchesKnn(target_clp, target_kp, source_clp, source_kp, matches, None, flags=2)
    cv2.imshow('img', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 距離を算出しているので、数値が小さいほど類似度が高いといえる
    rat = sum(similar) / len(similar)
    print('中間類似度：' + str(w) + ' : ' + str(rat))
    ratio.append(rat)

# 全類似度の平均をとってみる
ret_all = sum(ratio) / len(ratio)
print('【最終類似度】: ' + str(ret_all))
