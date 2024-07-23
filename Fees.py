import streamlit as st
import pandas as pd
db = pd.read_csv("Fee.csv")

task = """create a simple page for a school. Show on the page the Elementary fee is 5,000 dollars and the college fee is 25,000 dollars

Ask the parent name, address
Ask how many kids the parent have for elementary and ask if they have for college

create a csv file database to store this information with a submit button

Then show them their total tuition fee"""

st.title("High and middle School Fee app")

st.write("The school Fee per month is $500")

if st.checkbox("Do you want to sign up?"):

    st.write("to sighn up you need to fill this information.")
    
    #information
    Pname = st.text_input("Parents Name",placeholder = "I am: ")

    address = st.text_input("Full Address",placeholder = "Where do I live?")

    AgeL =  [i for i in range(0,6)]
    KidA = st.select_slider('Choose the number of kids in High school',AgeL)

    Age =  [i for i in range(0,6)]
    collageA = st.select_slider('Choose the number of kids in middle school',Age)
    
    High = KidA * 5000
    Middle = collageA * 5000
    Total = High + Middle

    CList = { "High":[High],"Middle":[Middle],"Total":[Total]}
    DataB = pd.concat([db,CList])
    DataB.to_csv("Fee.csv")   