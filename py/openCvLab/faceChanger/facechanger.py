import os
import cv2

"""
顔に画像を乗せる処理 
"""
# 作業ベースディレクトリ
base_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)))
# 画像ファイル名
target_path = os.path.join(base_dir, 'pyladies.png')
# imageの取得
target = cv2.imread(target_path)

# 画像のグレースケール化
target_gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)

# 顔検出モデル
cascade_path = os.path.join(base_dir, 'haarcascade_frontalface_default.xml')
cascade_model = cv2.CascadeClassifier(cascade_path)
# 顔検出
rectangles = cascade_model.detectMultiScale(target_gray)

# 置き換える画像
new_face_path = os.path.join(base_dir, 'tokyo.jpg')
new_face = cv2.imread(new_face_path)

# 画像を載せる処理(1枚に複数の顔があったら全部に処理かけるよ～）
for x, y, face_width, face_height in rectangles:
    # 顔のサイズに置き換え画像をリサイズ
    adjust_new_face = cv2.resize(new_face, (face_width, face_height))

    # 顔に新しい顔を上書き
    target[y: face_height + y, x: face_width + x] = adjust_new_face

# ファイル書き出し
cv2.imwrite('result.jpg', target)


