import streamlit as st
# classwork:
# create a list.py file
# -tell us what a list is in python
# -create an example of a list and display it in python
# -give 3 examples of how to use a list in streamlit
Cat = "cat"
Cow = "cow"
#1
list = [Cat,Cow,"hello"]

#2
st.write("A list is a variable where you can store more the one data by index.")

#3
st.write("this is a list",list,"= list")

#4 last
Radio = """Example 1: radio
Radio is a function in streamlit gives out information where you choose only 1:"""

st.write(Radio)
radio = st.radio("Radio",["hello","hi","good"])
st.write(radio)

st.write("""Example 2: SelectBox\n
A selectbox is a box which wen you cklick it shows you diferent options and as in the radio but without buttons.""")
Select = st.selectbox("SelectBox",["hello","Hi","Good"])
st.write(Select)
