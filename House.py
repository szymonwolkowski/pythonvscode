#settings
import streamlit as st 

#Introduction to the user

st.title("Welkome to house choosing app.")
st.sidebar.write("""**How to use the App?:** \nType in youre salary per year and the
                 House App would tell you what house can you buy. """)
for x in range(6):
  st.text("")


#Recive and calculate
House = None
Left, Right = st.columns(2)
with Left:
  money = st.number_input("Enter yearly salary:")
with Right:
  if st.button("Enter"):
    if money > 1_000_000:
      House = "A Mansion"
    elif money > 500_000:
      House = "A Duplex"
    elif money > 100_000:
      House = "A Bungalow"
    else:
      House = "nothing"


#output
if House:
  st.write("You can buy",House)