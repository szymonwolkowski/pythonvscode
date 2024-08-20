import streamlit as st
#inputs

st.title("How much do you **weight**")
weight = st.number_input("height",label_visibility='collapsed')
"""




"""
st.title("How tall are you in **CM**")
length = st.number_input('weight',label_visibility='collapsed')
hight = length ** 2

#outputs
p = "you are"
if st.button("submit"):
    mbi = float(weight) / float(hight)
    if mbi < 21:
        st.warning("UnderWeight")
    elif mbi > 21 and mbi < 24:
        st.success("Healthy in weight")
    elif mbi > 24 and mbi <27:
        st.warning("OverWeight")
    else:
        st.error("Obese")
