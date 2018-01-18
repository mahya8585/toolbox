from PIL import Image
import os

'''
指定の大きさに切り取る処理
'''
BASE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image')
IMAGE_DIR = os.path.join(BASE_DIR, 'target')
OUTPUT_DIR = os.path.join(BASE_DIR, 'result')

for image in os.listdir(IMAGE_DIR):
    if image == '__init__.py':
        continue

    # imageの取得
    im = Image.open(os.path.join(IMAGE_DIR,image))

    # 画像の切り取り
    # im.crop(左上X, 左上Y, 右下X, 右下Y)
    im_crop = im.crop((292, 203, 1694, 830))

    # ファイルの書き出し
    im_crop.save(os.path.join(OUTPUT_DIR,image), quality=100)
