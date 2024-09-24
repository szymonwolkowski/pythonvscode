#Settings and sets
import streamlit as st
from email.message import EmailMessage
import ssl
import smtplib
sender = 'p98666253@gmail.com'
Log = "_fMW,FYw4XH2X-k"
reciver = st.text_input("Enter Email of Reciever")
Sub = st.text_input("Enter subject")
Con = st.text_area("Enter content",height = 155)

if st.button("Send") and reciver and Sub and Con:
    email = EmailMessage()
    email["From"] = sender
    email["To"] = reciver
    email['subject'] = Sub
    email.set_content(Con)

    sec = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=sec) as smtp:
        smtp.login(sender,Log)
        smtp.sendmail(sender,reciver,email.as_string())
        st.success("Gmail sent!")