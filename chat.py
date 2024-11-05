#settings and basic variables
import streamlit as st
import pandas as pd
import os
db = pd.read_csv("chat.csv")
userid = str(len(db))

st.set_page_config(initial_sidebar_state="expanded")
#text entering and procesing 
n=st.sidebar.text_input("Name:")
t=st.sidebar.text_area("Text:")
OP = st.sidebar.radio("Pictures",["Yes","No"], horizontal=True)
if OP == "Yes":
    PD = st.sidebar.radio("Picture or Upload",["Choose",'Snap','Upload'],horizontal=True)
    if PD == "Snap":
        IM = st.sidebar.camera_input("make a snap")
        if IM:
            IMname = f'{userid}.png'
            with open (IMname,'wb') as writeimage:
                writeimage.write(IM.getbuffer())
    if PD == "Upload": 
        IM = st.sidebar.file_uploader("Upload Your Picture",type = ['jpg','jpeg','gif','png','tiff','WebP'])

        if IM:
            IMname = f'{userid}.png'
            with open (IMname,'wb') as writeimage:
                writeimage.write(IM.getbuffer())


#if (n and t):
#    Text = n+":  "+t
#sending
l,s,r = st.sidebar.columns(3)
with l:
    if st.sidebar.button("Send"):
        if (t and n):
            CSVl = {'userid':[userid],"Name":[n],"ChatText":[t]}
            CSVL = pd.DataFrame(CSVl)
            TO = pd.concat([CSVL, db], ignore_index = True)
            TO.to_csv('chat.csv', index = False)
with s:
    st.sidebar.button("refresh")



for i,row in db.iterrows():
    name,chattext = row["Name"],row["ChatText"]
    image = f'{row["userid"]}.png'
    
    col1,col2,col3 = st.columns([1,3,2])
    col1.write(name)
    
    col2.write(chattext)
    
    if os.path.exists(image):
        col3.image(image)
    else:
        col3.write("No image uploaded")

