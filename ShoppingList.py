import streamlit as st

# session state generation
if "list" not in st.session_state:
    st.session_state.list = []

# list code
loop = st.number_input("Whow many things are in the list.")
for x in loop:
    st.write("hello")