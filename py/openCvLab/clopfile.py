import cv2
import os

# 画像を分割する処理

IMAGE_DIR = os.path.abspath(os.path.dirname(__file__)) + '/comparison/'

# 比較元の画像抽出
SOURCE_FILE_NAME = '1.png'
source = cv2.imread(IMAGE_DIR + SOURCE_FILE_NAME)

# 画像の分割 今回はためしに縦に4分割
split_count = 4
height, width, channels = source.shape
new_width = int(width / split_count)
for w in range(split_count):
    width_start = w * new_width
    width_end = width_start + new_width

    file_name = "test_" + str(w) + ".png"
    clp = source[0:height, width_start:width_end]
    cv2.imwrite(file_name, clp)