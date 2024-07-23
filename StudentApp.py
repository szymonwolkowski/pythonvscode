#Settings
import streamlit as st
import pandas as pd
#import plotly.express as px
interactionL = {"rude":-20,"ignoring":-15,'disturbing':-15,"Helpful":20,"Paying an high amount of attention":35,
                "kind to everyone":40}
interactionP = 0
skills = {"creative":70,"smart":60,"automatic":40,"accurate":70,"sharing thoughts":65}
sub = False

#section setter
menu = st.sidebar.selectbox('Menu',["student sign up",'database|chart','Search'])

#Studen sighn up
if menu == 'student sign up':
    name = st.text_input("Whats student name?")
    left,right = st.columns(2)
    with left:
        math = st.number_input("Enter maths score:",0,100)
        english = st.number_input("Enter english score",0,100)
    with right:
        science = st.number_input("Enter Science score",0,100)
        interaction = st.multiselect("How does He/She act in class",list(interactionL.keys()))
        total = english + math + science
        avarege = total/3
    skill = st.radio("Best skill:",skills)    

    #calc interaction
    for i in interaction:
         interactionP += interactionL[i]
    if st.button("Submit scores."):
        st.success("Submit")
        st.write(name,"your interaction points are",interactionP,"your total score is,",total,"and your avarege is",avarege)
