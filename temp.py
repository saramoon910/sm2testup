"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st

import numpy as np
from mtcnn import MTCNN
from PIL import Image
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<meta charset="utf-8">
		<title>みんなのプライバシーを守り隊</title>
        
st.title("みんなのプライバシーを守り隊！どんな写真もまかセロリ！安心してアップしよう")

st.title("⬇ここに写真をアップロードしてね")
# 画像ファイルをアップロードするためのウィジェット
imgfile = st.file_uploader("Upload Image", type=["png", "jpg"], accept_multiple_files=False)

# 画像ファイルがアップロードされていなければ何もしない
if imgfile is not None:    
    img = Image.open(imgfile)

    # マスクのイラストの画像
    glass = Image.open('glass.png')

    # 元の画像を表示
    st.write("元の画像")
    st.image(img, use_column_width=True)

    # 画像に写っている顔を検出する
    detector = MTCNN()  
    # 検出された顔ごとに，顔のBounding Box，顔である確率，目や鼻などのKeypointsが得られる． 
    results = detector.detect_faces(np.asarray(img))
    for result in results:
        # 顔である確率
        confidence = result["confidence"]

        # 顔である確率が90%以下ならスルー
        if confidence < 0.9:
            continue

        # 顔のBounding Box
        x, y, w, h = result["box"]

        # マスクの画像を顔のサイズに合わせる．
        glass_resized = glass.resize((w, h*3//2)) 

        # マスクの画像を，検出された顔に貼り付ける．       
        img.paste(glass_resized, (x, y-h*1//3), glass_resized.convert("RGBA"))

    pil_img = Image.fromarray(np.uint8(img))

    st.write("サングラスを付けた画像")
    st.image(pil_img, use_column_width=True)
    
   </html>