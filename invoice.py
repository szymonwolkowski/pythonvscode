import streamlit as st
st.subheader("Invoice")
Country = "UAE"
street = "gjklajkfgl"
city = "Sharja"
st.sidebar.checkbox

Left,Right = st.columns(2)
st.write(Country)
st.write(city)
st.write(street)
st.write("\n")
st.write("Bill To:")
with Left:
    st.text_input("Enter name:",label_visibility="collapsed",placeholder="Name:")
    st.text_input("Enter mail:",label_visibility="collapsed",placeholder="Gmail")
with Right:
    RL,RR = st.columns(2)
    with RL:
        st.write("Invoice#")
        st.write("Invoice Date")