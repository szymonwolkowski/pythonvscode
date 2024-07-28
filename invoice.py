import streamlit as st
st.subheader("Invoice")
Country = "UAE"
street = "gjklajkfgl"
city = "Sharja"
T = st.sidebar.radio("Invoice",["Invoice generator","Location Edit"])
if T == "Invoice generator":
    st.write(Country)
    st.write(city)
    st.write(street)
    st.write("\n")
    st.write("Bill To:")
    Left,Right = st.columns(2)
    with Left:
        st.text_input("Enter name:",label_visibility="collapsed",placeholder="Name:")
        st.text_input("Enter mail:",label_visibility="collapsed",placeholder="Gmail")
    with Right:
        RL,RR = st.columns(2)
        with RL:
            st.write("Invoice#")
            st.write("Invoice Date")
            st.write("Due Date")
        with RR:
            st.text_input("Invoice#",label_visibility = "collapsed")
            st.date_input("Invoice date",label_visibility = "collapsed")
            st.date_input("Due date",label_visibility = "collapsed")
