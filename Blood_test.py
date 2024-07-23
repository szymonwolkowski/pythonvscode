task = """Create a menu for Registration and Database
Design a blood donation database that can get donor input
-Name -Contact Number (use text)
-Blood group (use radio or selectbox) -Disease/Infection (use radio or selectbox)

-Submit donor details

Next, save these in a csv file and show the database in a Database page in the menu"""
#settings
import streamlit as st
import pandas as pd
st.set_page_config(layout = "wide")
db = pd.read_csv("blood.csv",dtype={'Contact Number':str})

menu = st.sidebar.selectbox("menu",["SignUp","DataBase"])

if menu == "SignUp":
  #inputs
  left,right = st.columns(2)

  with left:
    Name = st.text_input("Enter name:")
  with right:
    ContactN =  st.text_input("Enter contact number:")
 
  with left:  
    BlTy = st.selectbox("Enter blood type",["A","AB","B","O"])
  with right:
    st.write('')
    st.write('')
    Save = "Save to table"
    #data base
    if st.button(Save):
      Tdict = {"Name":[Name],"Contact Number":[ContactN],"Blood Type":[BlTy]}
      VarTable = pd.DataFrame(Tdict)
      NewDf = pd.concat([db,VarTable],ignore_index=True)
      NewDf.to_csv("Blood.csv",index = False)
      st.success("save")
guards = {"1":"Doctor","2":"Nurse","3":"Reception"}



if menu == "DataBase":
  st.sidebar.write("Only guardians allowed",guards)
  left,right = st.columns(2)
  CPass = "8965Hope"
  TableBoo = False
  with left:

    passw = st.sidebar.text_input("Enter Guard Password",type = "password")
  with right:
    if st.sidebar.button("Enter"):
      if passw:
        if passw == CPass:
          TableBoo = True
        else:
          st.sidebar.error("error: \n wrong pass")
      else:
        st.sidebar.write("Enter password:")
  if TableBoo:
    st.dataframe(db,use_container_width= True)