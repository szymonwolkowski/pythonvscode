import streamlit as st

bill = 0  
menu = st.sidebar.subheader("orderd")
side1,side2,side3,side4 = st.columns(4)

meal1,meal2,meal3,meal4 = st.columns(4)

def meal1():
    st.image("https://pixabay.com/photos/prawn-seafood-shrimps-asian-1239427/")
    if st.checkbox("SuperShrimps"):
        bill += 10
        with side1:
            st.image("https://pixabay.com/photos/prawn-seafood-shrimps-asian-1239427/")


def meal2():
    st.image("https://pixabay.com/photos/prawn-seafood-shrimps-asian-1239427/")
    if st.checkbox("SushiSet"):
        bill += 60
        with side2:
            st.image("https://pixabay.com/photos/prawn-seafood-shrimps-asian-1239427/")


def meal3():
    st.image("https://pixabay.com/photos/salmon-fish-seafood-silver-skin-3139387/")
    if st.checkbox("SmokedSalmon"):
        bill += 25
        with side3:
            st.image("https://pixabay.com/photos/salmon-fish-seafood-silver-skin-3139387/")

def meal4():
    st.image("https://pixabay.com/photos/salmon-fish-seafood-silver-skin-3139387/")
    if st.checkbox("SmokedSalmon"):
        bill += 25
        with side4:
            st.image("https://pixabay.com/photos/salmon-fish-seafood-silver-skin-3139387/")

