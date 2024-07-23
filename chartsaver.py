import streamlit as st
import pandas as pd
import plotly.express as pl
st.title("Upload data to chart")
upload1,upload2 = st.columns(2)

with upload1:
    file_uploader = st.file_uploader("upload csv File",type="csv")
    
    if file_uploader:
        uploadcsv = pd.read_csv(file_uploader)
        choosesub = st.multiselect("Choose subject to plot",uploadcsv) 
        
        if choosesub:
            chart = st.dataframe(choosesub)
            pl.pie(chart)

        
        