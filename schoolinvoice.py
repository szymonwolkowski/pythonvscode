# schoolfees invoice (multipage menu)
# first page (REGISTER STUDENT)
# -ask to register student
# name, class, parentname, email, phone, address
# ---
# second page (ADD PAYMENT)
# -then add schoolfees payment section,
# search studentID (show student name and class) using PANDAS
# then choose year and session/term like '2024 first term' in dropdown
# and enter fees made with date input (students can make multiple payments in each session,(idea:list to add ))
# third page (DOWNLOAD RECIEPTS)
# search studentID (show name and year of student to confirm search) using PANDAS
# -filter per year and per session/term  '2024 first term' etc 
# download the payment invoice above using FPDF
# forth page (ADMIN ROLES)
# delete student or payment using PANDAS
# add new year session (for teachers to include new year/session/terms)

import pandas as pd
import streamlit as st

menu = st.sidebar.selectbox("Menu",["SighnUp","Fees","IDsearch","AnminSetting"])

st.title("Student and parent information:")
l,r = st.columns(2)

with l:
    child = st.text_input("Enter child name")
    gmail = st.text_input("Enter gmail")
with r:
    parent = st.text_input("Enter parend/guardian name")
    phone = st.text_input("Enter phone number", placeholder = "### ### ####")
st.divider()
st.title("School concepts")
L, R = st.columns(2)
with L:
    age = st.text_input("Age")
with R:
    Grade = []
    i = 0
    while i < 9:
        i+=1
        Grade.append('Grade '+str(i))
    grade = st.selectbox("Enter Grade",Grade)


