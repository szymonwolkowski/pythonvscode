import pandas as pd
import streamlit as st
st.title("private School application form")

menu = st.sidebar.selectbox('Menu',['Register Here','Database'])


db = pd.read_csv("schoolApp.csv")


if menu == 'Database':
    st.table(db)


if menu == 'Register Here':
    left,right = st.columns(2)

    #left
    with left:
        FName = st.text_input("Enter Parent full name",placeholder="First Name")
        AgeVar = [i for i in range(1,19)]
        Age = st.select_slider("Choose Child age", AgeVar)
        CFName = st.text_input("Enter Child Name",placeholder="first Name")
        Contact = st.text_input("Enter contact number:",placeholder="### ### ####")



    #right
    with right:
        Lname = st.text_input("last name",placeholder="Last Name", label_visibility= "hidden")
        Gender = st.radio("Enter gender",["Male","Female"])
        CLName = st.text_input("Enter child last name",label_visibility="hidden",placeholder="last name")
        Gmail = st.text_input("Enter G mail")

    school = st.text_input("Enter Child school:")

    #Address

    N1 , N2 , N3 = st.columns(3)

    with N1:
        street = st.text_input("Enter street:")
    
    with N2:
        continent = st.selectbox("Choose continent",["Asia","Africa","North America","South America","Europ","Astralia"])
        Zip = st.text_input("Enter Zip code:")



    with N3:
        country = st.text_input("Enter country")

    if st.button("submit"):
        columnList = {"Parent First name":[FName],"Last name":[Lname],"Age":[Age],"Gender":[Gender],
                                "Child's First name":[CFName],"Last name":[CLName],"Contact number":[Contact],"Gmail":[Gmail],
                                "Child's school":[school],"Street":[street],"Continent":[continent],
                                "Country":[country],"Zip":[Zip]}

        column = pd.DataFrame(columnList)
        DataB = pd.concat([db,column],ignore_index = True)
        DataB.to_csv('schoolApp.csv',index=False)
        st.success('Saved')

        