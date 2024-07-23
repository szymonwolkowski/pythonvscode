import streamlit as st
list = [i for i in range(1,101)]
st.selectbox("hi",list,label_visibility="collapsed")