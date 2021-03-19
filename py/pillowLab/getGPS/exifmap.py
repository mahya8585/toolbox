from pathlib import Path
from io import BytesIO
from PIL import Image
import PIL.ExifTags as ExifTags
import csv
import requests
import json

source_file = Path.cwd().joinpath('VendingMachine - upload-data.tsv')
result_file = Path.cwd().joinpath('glide.tsv')
get_photo_url = 'https://gvb58'

# データファイルを取得する (TSV)
output_data = []
with open(source_file, 'r', encoding='utf8') as source_tsv:
    tsv_file = csv.reader(source_tsv, delimiter='\t', doublequote=True, lineterminator='\n')

    for row in tsv_file:
        # 画像URLから画像を取得する
        if row[1].startswith('https') is False:
            continue

        # (認証が面倒だったのでGoogleドライブへの写真取得はLogic Appでチートしています)
        headers = {'content-type': 'application/json'}
        payload = {'id': row[1].split('id=')[1]}
        photo = requests.post(get_photo_url, data=json.dumps(payload), headers=headers)
        im = Image.open(BytesIO(photo.content))

        # exifからGPS情報を取得する
        exif = im._getexif()
        for k, v in exif.items():
            if k in ExifTags.TAGS:
                gps_tag = ExifTags.TAGS[k]
                # print(gps_tag, ":", v)

                if gps_tag == 'GPSInfo':
                    # 緯度経度の計算をする
                    lat_deg, lat_min, lat_sec = v[2][0], v[2][1], v[2][2]
                    latitude_n = lat_deg + (lat_min / 60.0) + (lat_sec / 3600.0)

                    lon_deg, lon_min, lon_sec = v[4][0], v[4][1], v[4][2]
                    longitude_e = lon_deg + (lon_min / 60.0) + (lon_sec / 3600.0)

                    # "緯度, 軽度" の形にデータ整形
                    # print(latitude_n, ', ', longitude_e)
                    row.append(str(latitude_n) + ', ' + str(longitude_e))
                    output_data.append('\t'.join(row))

# TSV出力
with open(result_file, mode='w', encoding='utf8') as f:
    f.write('\n'.join(output_data))

