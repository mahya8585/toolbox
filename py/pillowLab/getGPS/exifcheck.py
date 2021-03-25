from PIL import Image
import PIL.ExifTags as ExifTags
import os

img_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'img')

for image in os.listdir(img_dir):
    if image == '__init__.py':
        continue

    im = Image.open(os.path.join(img_dir, image))
    print('### ', image, ' ###')
    # exifからGPS情報を取得する
    exif = im._getexif()
    for k, v in exif.items():
        if k in ExifTags.TAGS:
            gps_tag = ExifTags.TAGS[k]
            print(gps_tag, ":", v)

            if gps_tag == 'GPSInfo':
                # 緯度経度の計算をする
                lat_deg, lat_min, lat_sec = v[2][0], v[2][1], v[2][2]
                latitude_n = lat_deg + (lat_min / 60.0) + (lat_sec / 3600.0)

                lon_deg, lon_min, lon_sec = v[4][0], v[4][1], v[4][2]
                longitude_e = lon_deg + (lon_min / 60.0) + (lon_sec / 3600.0)

                # print(latitude_n, ', ', longitude_e)



