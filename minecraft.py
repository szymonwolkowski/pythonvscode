#settings
import streamlit as st


#Design
st.title("Welkome to the minecraft price calculator.")
st.text("""**Instructions:** \n Enter the information about what you are going to choose,
        press enter and get the calculations of How much money will your game cost.\n \n \n""")
st.text('Are you sure you want to download minecraft? It costs $200.')


#Var
Cash = 0
Username = ""
Password = ""
World = ""

#input
if st.checkbox("Start calculating"):
    Cash += 200
    Username = st.text_input("Username:")
    Password = st.text_input("Password:",type="password")
    if Username and Password:
        World = st.radio("Choose type of world",['None',"Survival","Creative"])
        if World == "Survival":
            Cash += 20
            st.success(f"Survival mode bought and your minecraft total costs {Cash} dollars.")
        elif World == 'Creative':
            Cash += 100
            st.success(f"Creative mode bought and your minecraft total costs {Cash} dollars.")
        

            





#output/readybutton