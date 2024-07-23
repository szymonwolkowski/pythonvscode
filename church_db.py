# create a simple church age range database (Registration, Database page)

# This will get the name, age, (2 columns)   


#gender of the church memeber with a submit button (2 columns)

# save this in a database and display on a new page (this page MUST have a login feature)

# Make sure you group members in differnt category based on their age fdgdf 
#
# (Kids(3- 12), Teens(13-19), Youth(20-35), Adult(36-64), Elders(65+) )
# save all information in a csv file

#settings
import streamlit as st
import pandas as pd
db = pd.read_csv("CHurch_people.csv")
st.set_page_config(layout = "wide")
choose = st.sidebar.selectbox("SighnUp or SeeTheList",["sighn up","see list"])
submit = False

#inputs
if choose == "sighn up":
    left,right = st.columns(2)
    with left:
        name = st.text_input("Enter name") #name
        gender = st.radio("gender",["male","femail"]) #gender
    with right:
        Age = st.text_input("Enter age") #age
        if st.button("submit"):
            submit = True
    if submit:
        DataList = pd.DataFrame({"Age":[Age],"Gender":[gender],"Name":name})
        DataFrame = pd.concat([db,DataList],ignore_index = True)
        DataFrame.to_csv("CHurch_people.csv",index = False)

if choose == "see list":
    CPass = "896722fire"
    password = st.sidebar.text_input("Enter password")
    if st.sidebar.button("Login"):
        if password:
            if password == CPass:
                st.dataframe(db,use_container_width = True)
