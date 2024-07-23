#Project Objective
# Create a student scores database which can 
# -get the name
# -4 subjects
# -calculate the average/mean of all the scores
# -calculate the grade (A,B,C,D,E,F)
# -save and update in a csv file
import streamlit as st
import pandas as pd
countries = pd.read_csv("countries.csv") #pandas will help you open your csv file and display as a table (dataframe)
#What is a CSV file?
#csv file is a text file that each data is separated by a comma (comma separated values)
#display
st.set_page_config(layout = 'wide')
df = pd.read_csv("scores.csv")

st.table(df)

Name = st.text_input("my name is:")
left,right = st.columns(2)
#inputs

with left:
  English = st.number_input("My english score is:",0,100)
with right:
  Maths = st.number_input("My maths score is:",0,100)
with left:
  Science = st.number_input("My science score is:",0,100)
with right:
  Ict = st.number_input("My ict score is:",0,100)
total = Ict + Science + Maths + English
average = total / 4

#grade
if   average > 90 - 1:
  grade = "A+"
elif average > 80 - 1:
  grade = "B+"
elif average > 70 - 1:
  grade = "C+"
elif average > 60 - 1:
  grade = "D"
elif average > 50 - 1:
  grade = "E"
else:
  grade = "F-"

#new student button
if st.button("submit"):
  AddDict = {"Name":[Name],"English":[English],"Maths":[Maths],"Science":[Science],"Ict":[Ict],
                        "Average":[average],"Total":[total],"Grade":[grade]}
  AddDf = pd.DataFrame(AddDict)
  # st.dataframe(AddDf)
  newDf = pd.concat([df,AddDf],ignore_index=True)
  newDf.to_csv("scores.csv",index=False)

