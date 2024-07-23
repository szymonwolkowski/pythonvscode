import streamlit as st
st.title("Whelkome to hospital register")
left,right = st.columns(2)

with left:
    title = st.radio("CHoose title:",["Mr","Mrs","Dr"],horizontal = True)
    Name = st.text_input("Enter name")
    lName = st.text_input("Enter last name")
    DateOfB = st.date_input("Enter date fo birth")
st.title("Parent contact deatails:")
left2,right2 = st.columns(2)
with left2:  
    FN = st.text_input("Enter phone number:")
    City = st.text_input("City/town")

with right:
    DateOfR = st.date_input("Enter date of registration:")
    NiName = st.text_input("Enter Nick name:")
    LNamest = st.text_input("Enter last name:")
    PName = st.text_input("Enter preffered name:")

with right2:
    st.text_input("Addres")