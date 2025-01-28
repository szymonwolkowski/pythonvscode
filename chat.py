#settings and basic variables
import streamlit as st
import pandas as pd
import os
try:
    chat = pd.read_csv("chataccounts.csv")
except:
    pd.DataFrame()

db = pd.read_csv("chat.csv")
userid = str(len(db))

menu = st.sidebar.selectbox('Sighnup or login',["Sighnup","Login"])
if menu == "Sighnup":
    avatar = st.file_uploader("Upload your Image",type=("jpg","png","jpeg"))
    user = st.text_input("user",placeholder= "Username",label_visibility="collapsed")
    l,r = st.columns(2)
    with l:
        password = st.text_input("user",placeholder= "Password",label_visibility="collapsed",type="password")
        email = st.text_input("user",placeholder= "Gmail",label_visibility="collapsed")
    with r:
        confirmp = st.text_input("user",placeholder= "Confirm your Password",label_visibility="collapsed",type="password")
        fname = st.text_input("user",placeholder= "First Name",label_visibility="collapsed")
    fullname= st.text_input("user",placeholder= "Enter your full name",label_visibility="collapsed")
    if st.button("Done"):
        if password and email and avatar and user and confirmp and fname and fullname:
            if password == confirmp:
                if "@" in email and ".com" in email and " " not in email:
                    imagename = f"{email}.png"
                    with open(imagename,"wb") as writename:
                        writename.write(avatar.getbuffer())
                
                    UDict = {"username":[user],"password":[password],"confirmp":[confirmp],"First name":[fname],"Fullname":[fullname]}
                    Key = pd.DataFrame(UDict)
                    Key.to_csv("chataccounts.csv",index=False)

if menu == "Login":
    usern=st.sidebar.text_input("Enter username")
    passw=st.sidebar.text_input("Enter password")
    if usern and passw:
        if st.sidebar.checkbox("login"):
            try:
                findN = chat[chat["username"] == usern]
                getuser = findN["username"].iloc[0]
                getpass = findN["password"].iloc[0]
                if usern.lower() == str(getpass).lower() and str(passw) == str(getpass).lower():
                    st.write("correct")
                else:
                    st.error("Wrong Password!")
            except IndexError:
                st.error("Sorry, This Username dosent exist!")