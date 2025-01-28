import streamlit as st

st.title("Welkome to our donation app!")
st.text("This is where you set money goals and make campins")
l,r = st.columns(2)
with l:
    name = st.text_input("Name your campaingn.")
with r:
    gmail = st.text_input("Enter your Gmail for us to inform you.")
st.divider()

information = st.text_area("Give some deeper information about your campaign.",200,100)

num = st.selectbox("Choose Your Money Goal",[5,10,20,30,40,50,100,200,300,350,"Type your own."])
if num == "Type your own.":
    num = st.number_input("Enter the amount:",1,100000,value=10000)