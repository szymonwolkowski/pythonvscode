import streamlit as st

if "number" not in st.session_state():
    st.session_state.number = 5

if st.button("+1"):
    st.session_state.number += 1
st.write(st.session_state.number88)