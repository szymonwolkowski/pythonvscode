#settings and basic variables
import streamlit as st
import pandas as pd
db = pd.read_csv("chat.csv")
Text = None

#text entering and procesing 
n=st.text_input("Name:")
t=st.text_area("Text:")

if (n and t):
    Text = n+":  "+t
#sending
r,l,s = st.columns(3)
with r:
    if st.button("Send"):
        if (Text):
            CSVl = {"ChatText":[Text]}
            CSVL = pd.DataFrame(CSVl)
            TO = pd.concat([CSVL, db], ignore_index = True)
            TO.to_csv('chat.csv', index = False)
with l:
    st.button("refresh")
st.table(db)             #Table <---