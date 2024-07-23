import streamlit as st
TInt = int(st.text_input("Enter timer"))
times = None
while TInt != times:
    st.write(TInt)
    times = times + 1
