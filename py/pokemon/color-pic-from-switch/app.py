from PIL import ImageGrab
import numpy as np
import cv2
import winsound
# from playsound import playsound
import time


# 取得したい色の範囲を指定・抽出 (今回は例としてゴルバットの色違いを指定)
poke_pic_color_lower = np.array([76, 115, 84])
poke_pic_color_upper = np.array([114, 165, 86])

# 無限ループ★
while True:
    # 画面全体をキャプチャする(複数ディスプレイある時はメインディスプレイでSwitch動かしてね)
    im = ImageGrab.grab(all_screens=False)

    pic_color = cv2.inRange(np.array(im), poke_pic_color_lower, poke_pic_color_upper)
    # 実際取れた値を画像化チェック
    # im_ch = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
    # extraction = cv2.bitwise_and(im_ch, im_ch, mask=pic_color)
    # cv2.imwrite('target.jpg', extraction)

    found_it = False
    for line in pic_color:
        for pix in line:
            # 色の抽出ができていれば255が返ってくる
            if pix == 255:
                # アラート音を鳴らす
                winsound.PlaySound('DQ-levelup.wav', winsound.SND_FILENAME)
                # macの人はこっち
                # playsound('DQ-levelup.mp3')
                found_it = True
                break
        
        # 何回も鳴らすのはうるさいので、一回見つかったら終了
        if found_it:
            break
    
    # 停止時間を指定
    time.sleep(3)


