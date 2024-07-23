"""Test:
Create a simple python program that
-create a menu for student details and students database
-Ask for student name on the left column and their age on the right column
-create a submit button
- save this in a csv file
show the dataframe in database page 

"""
import streamlit as st 
import pandas as pd
mode = st.sidebar.radio("student information gathering.",["SignUp","DataTable"])
table = pd.read_csv('student.csv')

if mode == "SignUp":
    left, right = st.columns(2)
    with left:
        name = st.text_input("Enter Name")

    with right:
        age = st.text_input("Enter Age")
    if st.button("submit"):
        dict = {"Name":[name],"Age":[age]}
        database = pd.concat([dict,table],ignore_index=True)
        database.to_csv("student.csv",index = False)
if mode == "DataTable":
    st.dataframe(table)