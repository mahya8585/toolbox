from PIL import Image
import os

'''
指定の大きさに切り取る処理
'''

IMAGE_DIR = os.path.abspath(os.path.dirname(__file__)) + '/image/'
OUTPUT_DIR = IMAGE_DIR + 'result/'

# imageの取得
im = Image.open(IMAGE_DIR + 'danbo-mini.jpg')

# 画像の切り取り
# im.crop(左上X, 左上Y, 右下X, 右下Y)
im_crop = im.crop((292, 203, 1694, 830))

# ファイルの書き出し
im_crop.save(OUTPUT_DIR + 'extract.jpg', quality=100)