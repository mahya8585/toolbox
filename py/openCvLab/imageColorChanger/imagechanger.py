import cv2
import os
import numpy as np

"""
画像を色々編集してみよう 
"""
# 作業ベースディレクトリ
base_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)))
# 画像ファイル名
target_path = os.path.join(base_dir, 'images', 'queen.jpg')
# imageの取得
target = cv2.imread(target_path)

# グレースケール
gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray.jpg', gray)

# 色相変換(COLOR_BGR2HLS/COLOR_BGR2HSV/COLOR_BGR2YCrCb/COLOR_BGR2XYZ
# C:\Users\maishid\.PyCharmCE2019.3\system\python_stubs\376206279\cv2\cv2\__init__.py
change_color = cv2.cvtColor(target, cv2.COLOR_BGR2XYZ)
cv2.imwrite('change-color.jpg', change_color)

# カラーマップの適用(COLORMAP_AUTUMN/COLORMAP_BONE/COLORMAP_CIVIDISなどなど
# C:\Users\maishid\.PyCharmCE2019.3\system\python_stubs\376206279\cv2\cv2\__init__.py
color_map = cv2.applyColorMap(target, cv2.COLORMAP_TWILIGHT)
cv2.imwrite('color-map.jpg', color_map)

# 二値化
r, mono = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite('threshold.jpg', mono)

# 貼り絵風(二値化)
r, paste_picture = cv2.threshold(target, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite('paste-picture.jpg', paste_picture)

# 鉛筆画風(エッジ検出)
edge = cv2.Canny(target, 1, 255)
cv2.imwrite('pencil.jpg', edge)

# ネガポジ反転
inversion = cv2.bitwise_not(target)
cv2.imwrite('inversion.jpg', inversion)

# 色抽出
# 抽出する色の範囲(RGBじゃないくBGRの順番なのに注意)
bgr_lower = np.array([0, 0, 10])
bgr_upper = np.array([15, 15, 255])
# 指定色範囲を抽出
color_range = cv2.inRange(target, bgr_lower, bgr_upper)
extraction = cv2.bitwise_and(target, target, mask=color_range)
cv2.imwrite('extraction.jpg', extraction)

# 白黒色抜き(画像の合成)
gray_color = cv2.imread(os.path.join(base_dir, 'gray.jpg'))
composition = cv2.addWeighted(gray_color, 1, extraction, 0.9, 0)
cv2.imwrite('composition.jpg', composition)
