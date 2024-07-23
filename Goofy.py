# settings
import streamlit as st
st.title("Voting app")
Task = """Create a voting application program that accepts user input for 
their age and print to the screen whether or not they are eligible to vote.
Use minimum age as 18."""

#input
age = st.number_input("Wow old are you?:",1,150)

#output
if st.checkbox("Submit!"):
    if age < 18:
        st.warning("Sorry! You are to small to vote.")
    else:
        st.success("You Can Vote!")


