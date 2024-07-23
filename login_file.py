import streamlit as st
import pandas as pd
#correctpassword = csvlink['password'].iloc[0]
#Szymon should read a createa a loginfile.py
#show a database when a user login
#make sure you save the password in a CSV file

#inputs
csv = pd.read_csv("login.csv")
cpass = csv["password"].iloc[0]
if st.text_input("Enter Password:") == cpass:
    "welkome"