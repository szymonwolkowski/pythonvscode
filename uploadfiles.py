import streamlit as st
import pandas as pd 
menu = st.sidebar.selectbox("Upload type",["CSV","image","video","audio"])

if menu == 'CSV':
    CSV = st.file_uploader("upload CSV",type = "CSV")
    if CSV:
        csv=pd.read_csv(CSV)
        with st.expander("Get your CSV:"):
            st.table(csv)

elif menu == 'image':
    image = st.file_uploader("upload image",type = ('jpg', 'jpeg', 'png'))
    if image:
        with st.expander("Get your image:"):
            st.image(image)

elif menu == 'audio':
    audio = st.file_uploader("upload audio",type = "mp3")
    if audio:
        with st.expander("Get your audio:"):
            st.audio(audio)

else:
    video = st.file_uploader("upload video",type = "mp4")
    if video:
        with st.expander("Get your video:"):
            st.video(video)
