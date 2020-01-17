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
# matches = cv2.BFMatcher(cv2.NORM_HAMMING).knnMatch(source_des, target_des, k=2)
matches = cv2.BFMatcher(cv2.NORM_HAMMING).knnMatch(source_des, target_des, k=5)

# ratio test
# ratio = 0.75
# similar = []
# for m, n in matches:
#     if m.distance < ratio * n.distance:
#         similar.append([m])

similar = []
for m in matches:
    distances = [info.distance for info in m]
    ratio = sum(distances)/len(m)
    similar.append(ratio)


# 画像出力確認e
# output = cv2.drawMatchesKnn(target, target_kp, source, source_kp, matches, None, flags=5)
# cv2.imshow('img', output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# dist = []
# for match_list in similar:
#     dist.append(match_list[0].distance)
# ret = sum(dist) / len(dist)
ret = sum(similar) / len(similar)

# 距離を算出しているので、数値が小さいほど類似度が高いといえる
print('類似度：' + str(ret))
