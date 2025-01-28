import streamlit as st
import pandas as pd
import plotly.express as pe
att = pd.read_csv("attendance.csv")

if st.sidebar.toggle("Sighn students attendance."):
    L,R=st.sidebar.columns(2)
    with L:
        name = st.text_input("Students Name",placeholder="Name")
        present = st.number_input("present",1,365,value=365)
    with R:
        roll = st.number_input("roll number",1,value=1)
        apsent = st.number_input("apsent",1,365,value=365)

if st.button("Submit") and name and present and roll and apsent and (present + apsent > 306):
    Dict = {"name":[name],"present":[present],"roll":[roll],"apsent":[apsent]}
    CSVDict = pd.DataFrame(Dict)
    csvdict=pd.concat(CSVDict,att)
    csvdict.to_csv('attendance.csv')