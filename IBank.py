#Settings
import streamlit as st
import pandas as pd
db = pd.read_csv("Ibank.csv")
Menu = st.sidebar.radio("Menu",["Create","See"])
st.title("Welkome to information banK")


if Menu == "Create":
    Name = st.sidebar.text_input("Enter information name Here:",placeholder="Name")
    Pass = st.sidebar.text_input("Enter informaton password Here:",placeholder="4tcjf54u3%^^^2`1hi")
    Inf = st.text_input("Enter your **information** here:",placeholder="This is...")
    if st.sidebar.button("Submit"):
        if Name and Pass and Inf:
            List = {"Name":Name,"Pass":Pass,"Text":Inf}
            InfV = pd.DataFrame([List])
            DF = pd.concat([db,InfV],ignore_index = True)
            DF.to_csv("Ibank.csv", index=False)
            st.success("Saved")
        else:
            st.error("Information Incomplete")

else:
    Name = st.sidebar.text_input("Enter information name Here",placeholder="Name")
    result = pd.read_csv("Ibank.csv") # caly csv 
    option = st.selectbox("What information do you want to choose", result)

    st.write("You selected:", option)
    st.write("All data:", result.loc[result['Name'] == option])
    #st.write("All data:", result.loc[result['Name'].str.contains(option)])
