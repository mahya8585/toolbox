import cv2
import os

# 画像を比較して類似度を得る処理

IMAGE_DIR = os.path.abspath(os.path.dirname(__file__)) + '/comparison/'
# 画像サイズが一緒でない場合は画像サイズを合わせたほうがいい
# IMAGE_SIZE = (993, 449)

# 特徴量抽出処理の選定
# detector = cv2.AKAZE_create()
detector = cv2.ORB_create()

# 比較元の特徴量抽出(今回はグレースケールでの抽出とする)
SOURCE_FILE_NAME = '1.png'
source = cv2.imread(IMAGE_DIR + SOURCE_FILE_NAME, cv2.IMREAD_GRAYSCALE)
# source = cv2.resize(source, IMAGE_SIZE)

(source_kp, source_des) = detector.detectAndCompute(source, None)

# 比較対象の設定
TARGET_FILE_NAME = '2.png'
target = cv2.imread(IMAGE_DIR + TARGET_FILE_NAME, cv2.IMREAD_GRAYSCALE)
# target = cv2.resize(source, IMAGE_SIZE)

(target_kp, target_des) = detector.detectAndCompute(target, None)

# 類似度確認
matches = cv2.BFMatcher(cv2.NORM_HAMMING).match(source_des, target_des)
dist = [m.distance for m in matches]
ret = sum(dist) / len(dist)

# 距離を算出しているので、数値が小さいほど類似度が高いといえる
print(dist)
print('類似度：' + str(ret))
