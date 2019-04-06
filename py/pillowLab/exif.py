from PIL import Image
import os


base_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image')
img_dir = os.path.join(base_dir, 'target')
output_dir = os.path.join(base_dir, 'result')

# Orientation タグ値にしたがった処理
# PIL における Rotate の角度は反時計回りが正
convert_image = {
    1: lambda img: img,
    2: lambda img: img.transpose(Image.FLIP_LEFT_RIGHT),                              # 左右反転
    3: lambda img: img.transpose(Image.ROTATE_180),                                   # 180度回転
    4: lambda img: img.transpose(Image.FLIP_TOP_BOTTOM),                              # 上下反転
    5: lambda img: img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_90),   # 左右反転＆反時計回りに90度回転
    6: lambda img: img.transpose(Image.ROTATE_270),                                   # 反時計回りに270度回転
    7: lambda img: img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_270), # 左右反転＆反時計回りに270度回転
    8: lambda img: img.transpose(Image.ROTATE_90),                                    # 反時計回りに90度回転
}


for image in os.listdir(img_dir):
    if image == '__init__.py':
        continue

    img_path = os.path.join(img_dir, image)
    im = Image.open(img_path)

    exif = im._getexif()
    orientation = exif.get(0x112, 1)

    convert_img = convert_image[orientation](im)

    # ファイルの書き出し
    convert_img.save(os.path.join(output_dir, 'exif-' + image), quality=100)

