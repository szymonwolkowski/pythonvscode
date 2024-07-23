import streamlit as st 
import pandas as pd
display = pd.read_csv("schoolApp.csv")
st.set_page_config(layout = "wide")
Cpass = "1234"
st.title("No scores without password")
#password
password = st.sidebar.text_input("Enter Teacher password",type = "password")
if password:
    if password == Cpass:
        st.sidebar.success("correct password!")
        st.table(display)
    else:
        st.sidebar.error("wrong password!")
else: 
    st.sidebar.warning("no password")

#display
