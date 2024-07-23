import streamlit as st
import pandas as pd
#create a register and login side bar to allow many people to register (username, password)
#then ask them to login checking if their credentials are correct.
#display their name after a succesful login

df = pd.read_csv("reg.csv")
menu = st.sidebar.selectbox("login or sighnup",["login","sighnup"])

#sighnup
if menu == "sighnup":
    useN = st.text_input("Enter Username:")
    Password = st.text_input("Enter your wanted password:")
    #Csv saver \/
    if st.button("save"):
        CL = pd.DataFrame({"UserName":[useN],"Password":[Password]})
        DataFrame = pd.concat([CL,df].ig)
        DataFrame.to_csv("reg.csv")

#login
if menu == "login":
    pas = st.text_input("Enter your password:")
    try:
        CorUser = db["Password"].iloc[pas]
    except:
        st.error("wrong pass")
