#Settings
import streamlit as st
import pandas as pd 

try:
    db = pd.read_csv("vote.csv")
except pd.errors.EmptyDataError:
      db = pd.DataFrame()


#desighn and vote.
st.title("Welkome to voting app.")
st.text("You would need to fill these forms before vote.")
name = st.text_input("Enter your name")
vote = st.selectbox("Choose Your Vote",["Szymon","Lena","Avaneesh","Mateo","Vanya","Joan","Nicolai","Ana"])
if st.button("Vote"):
    if vote == "Szymon":
          V = {"szymon":[vote]}
    if vote == "Lena":
          V = {"Lena":[vote]}
    if vote == "Avaneesh":
          V = {"Avaneesh":[vote]}
    if vote == "Mateo":
          V = {"Mateo":[vote]} 
    if vote == "Vanya":
          V = {"Vanya":[vote]}
    if vote == "Joan":
          V = {"Joan":[vote]}
    if vote == "Nicolai":
          V = {"Nicolai":[vote]}
    if vote == "Ana":
          V = {"Ana":[vote]}
    Var = pd.DataFrame(V)
    TO = pd.concat([Var, db], ignore_index = True)
    TO.to_csv('vote.csv', index = False)