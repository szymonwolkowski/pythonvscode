#settings
import streamlit as st
import pandas as pd
st.set_page_config(layout = "wide")
#sidebar
menu = st.sidebar.selectbox("menu",["DataBase","SignUp"])
db = pd.read_csv("employ.csv")

if menu == "DataBase":
  st.title("Admin password reqired:")
  
  #passwordEntering
  Cpass = 1234
  pas = st.text_input("Enter Password:",type = "password")
  if st.button("Submit"):
    if pas:
      if pas == str(Cpass):
        st.dataframe(db)
      else:
        st.error("Wrong password")
    else:
      st.warning("Enter Password")

  

if menu == "SignUp":


  st.title("Employee registration") #title



  #inputs
  left, right = st.columns(2)
  with left: #left inputing
    fname = st.text_input("Enter your first name:")
    email = st.text_input("Enter email:")
    knowlage = st.selectbox("Education",["bad","medium","good","Expert","Master"])
    job = st.selectbox("department",["Engineering","Transport","Security","Health","Accounting"])
    Edate = st.date_input("Enter Employment date")

  with right: #right inputing
    lname = st.text_input("Enter last name:")
    gender = st.radio("Gender",["male","female"],horizontal = True)
    money = st.text_input("Enter monthly salary:")
    status = st.select_slider("Employee status",["full time","part time"])
    date = st.date_input("Enter todays Date:")
  if st.button("submit"):
    dfDict = pd.DataFrame({"First name":[fname],"Last name":[lname],"Email":[email],"Gender":[gender],
              "Education":[knowlage],"Money/Month":[money],"Department":[job],
              "SignUp Date":[date],'Employment Date':[Edate]})
    csvTable = pd.concat([db , dfDict],ignore_index= True)
    csvTable.to_csv("employ.csv",index=False)
    st.success("save")