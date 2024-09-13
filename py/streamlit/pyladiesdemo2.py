import streamlit as st
import pandas as pd

#  text input
name = st.text_input('名前を入力してください')
st.write('こんにちは', name)

# check box
agree = st.checkbox('画像を表示しますか？')
if agree:
    st.image('https://github.com/PyLadiesTokyo/python-beginners/blob/master/image_processing/images/pyladies-tokyo.png?raw=true', caption='githubから取得', use_column_width=False)

# multi select
options = st.multiselect(
    ' あなたの好きな本を選んでください',
    options=['青', '黄色', '赤', 'ピンク', '金色'],
    default=['青'],
)
st.write('好きな色:', options)

# slider
history = st.slider("Python歴は?", 0, 33, 3)
st.write("私のPython歴は ", history, "です")

# camera input
picture = st.camera_input("撮影!")

if picture:
    st.image(picture)

# file upload
uploaded_file = st.file_uploader('画像を選択してください', type=['jpg','png'])
if uploaded_file is not None:
    st.image(uploaded_file)

uploaded_csv_file = st.file_uploader('csvファイルを選択してください', type=['csv'])
if uploaded_csv_file is not None:
    df = pd.read_csv(uploaded_csv_file)
    st.write(df)

#sidebar
st.sidebar.text_input('名前を入力してください')