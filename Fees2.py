import streamlit as st
import pandas as pd
db = pd.read_csv("Fee.csv")
from time import sleep
st.title("Welkome to our school Fee sighn up.") 
st.text("High school fee is 15_000 and colage fee is 25_000")

if st.checkbox("Sighn Up Now"):
  sleep(1)
  st.write("You would need to fill those forms first")
  sleep(2)
  left,right = st.columns(2)

  with left:
    parent = st.text_input("Enter parent name")
    adress = st.text_input("Enter Adress",placeholder="Where do you live?") 
    schoolType = st.multiselect("Select if you have your kids in high school, colage or both",["colage","High school"])

  if schoolType:
    sleep(1)
    with right:
        if schoolType == "colage":
            collage = st.number_input("Whow many kids go for colage")  
        else: 
           collage = 0
        if schoolType == "High school":
            High = st.number_input("Whow many kids go for colage")
        else:
            High = 0
  if st.checkbox("submit"):
     VarDict = {"person":parent,'adress':adress,"collage":collage,'High':High,"total":collage+High}
     VarTable = pd.DataFrame(VarDict)
     DB = pd.concat([db ,VarTable],ignore_index = True)
     DB.to_csv("Fee.csv",index= False)
    
     st.text("the total is",(collage+High)*25000)