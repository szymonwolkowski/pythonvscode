import streamlit as st
var = """simple test

write a program for a use
-ask for the name and -age - use a radio to ask for gender
-use a selectbox to ask to choose best color - use a type to ask best game
-use a type to ask to type best movie - use a type to ask best friend
create a submit button and show this in a success bar
Jeida (F), your best game is: Minecraft, Color: Blue, Movie: Spiderman, Friend: Tofe"""

left,right = st.columns(2)
tick = False
with left:  #left side
    name = st.text_input("Enter name:")
    gender = st.radio("Gender",["male","female"],horizontal = True)
    game = st.text_input("Enter best video-game")
    submit = st.button("Submit")

with right:  #right side
  age = st.text_input("Enter age:")
  st.selectbox("Chose favorite color",["red",'orange',"yello",'green',"blue",'purple'])
  movie = st.text_input("Enter best movie")
  friend = st.text_input("Enter best friend:")

if submit:
    st.write("Gender is",gender,"\nName is",name,"you are",age,"years old, your best friend is",friend,", your favorite",
             "video game is",game,"and youre favorite movie is",movie,".")