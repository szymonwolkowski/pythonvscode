import streamlit as st
from fpdf import FPDF
import base64 
Country = "UAE"
street = "Zayed street"
city = "Sharja"
company = "workors"
BankN = "ADCB"
BankU = "S"
BankP = 123
T = st.sidebar.radio("Invoice",["Invoice generator","Location Edit"])
if T == "Invoice generator":
    LLL,RRR = st.columns(2)
    with RRR:
        p1,p2 = st.columns(2)
        with p2:
            st.subheader("Invoice")
    with LLL:
        logo1,logo2,logo3=st.columns(3)
        with logo1:
            st.image("Send.png")
        st.write(company)
        st.write(street)
        st.write(city)
        st.write(Country)
        st.write("\n")
        st.write("Bill To:")
    Left,Right = st.columns(2)
    with Left:
        name = st.text_input("Enter name:",label_visibility="collapsed",placeholder="Name:")
        email = st.text_input("Enter mail:",label_visibility="collapsed",placeholder="Gmail")
    with Right:
        RL,RR = st.columns(2)
        with RL:
            st.write("Invoice#")
            st.write("")
            st.write("Invoice Date")
            st.write("")
            st.write("Due Date")
        with RR:
            invoice = st.text_input("Invoice#",label_visibility = "collapsed")
            date = st.date_input("Invoice date",label_visibility = "collapsed")
            Ddate = st.date_input("Due date",label_visibility = "collapsed")
    L1,L2,L3,L4 = st.columns(4)
    
    #sidebar tax&Discount
    D = st.sidebar.number_input("Discount",0)
    T = st.sidebar.number_input('Tax',0)
    Dis = D/100
    Tax = T/100
    

    with L1:
        st.write("Descritpion")
        D = st.text_input("D",label_visibility= "collapsed")
    with L2:
        st.write("Quantity")
        Q = st.number_input("Q",0,label_visibility= "collapsed")
    with L3:
        st.write("Price|Unit")
        PU = st.number_input("PU",label_visibility="collapsed")
    with L4:
        st.write("Total price")
        taxcalc = (Tax) * (Q*PU)
        discalc = (Dis) * (Q*PU)
        price = int(PU * Q) 
        st.text_input("TP",label_visibility="collapsed",placeholder = PU * Q,disabled=True)    
    for i in range(2):
        st.divider()
    L,R = st.columns(2)
    with R:
        st.text("Payment Due")
        for i in range(3):
            st.write("")
        total = price +taxcalc-discalc
        price = (total)
        st.title(price)
    with L:
        BankU = st.text_input("Bank Name")
        st.write("Bank Username",BankU)
        st.write("Bank Password",BankP)        

            



    def generate_pdf(): ######################################Generate pdf
        pdf=FPDF() ###Make the variable
        pdf.add_page() ###Make page

        X =10
        Y =10
        W =90

        pdf.image("Send.png",x=X,y=Y,w=29)#image
        

        pdf.set_font("Courier",size=12)#company
        Y = Y + 35
        pdf.set_xy(x=X,y=Y)
        pdf.cell(w=100,txt=f"{company}", ln=True, align = True)

        pdf.set_font("Courier",size=12)#street
        Y = Y + 10
        pdf.set_xy(x=X,y=Y)
        pdf.cell(w=W,txt=f"{street}")

        pdf.set_font("Courier",size=12)#city
        Y = Y + 10
        pdf.set_xy(x=X,y=Y)
        pdf.cell(w=W,txt=f"{city}")

        pdf.set_font("Courier",size=12)
        Y = Y + 10
        pdf.set_xy(x=X,y=Y)
        pdf.cell(w=W,txt=f"{Country}")#country
        
        pdf.set_font("Arial",size=12,style = "B")#bill to
        Y = 110
        pdf.set_xy(x=X,y=Y-10)
        pdf.cell(w=W,txt="Bill to:")

        pdf.set_font("Arial",size=12,style = "B")#name 

        pdf.set_xy(x=X,y=Y)
        pdf.cell(w=W,txt=f"{name}")

        pdf.set_font("Arial",size=12,style = "B")#email
        pdf.set_xy(x=X,y=Y+10)
        pdf.cell(w=W,txt=f"{email}")

        pdf.set_font("Arial",size=15,style = "BI")
        pdf.set_xy(x=X+0,y=140)
        pdf.cell(w=W,txt="description")
        
        pdf.set_font("Arial",size=15,style = "BI")
        pdf.set_xy(x=X+60,y=140)
        pdf.cell(w=W,txt="quantity")

        pdf.set_font("Arial",size=15,style = "BI")
        pdf.set_xy(x=X+90,y=140)
        pdf.cell(w=W,txt="price|bill")

        pdf.set_font("Arial",size=15,style = "BI")
        pdf.set_xy(x=X+120,y=140)
        pdf.cell(w=W,txt="total price")
        Y = 160

        pdf.set_font("Arial",size = 15,style = "B")
        pdf.set_xy(x=X,y=Y)
        pdf.cell(w=90,txt=f"{D}")

        pdf.set_font("Arial",size = 15,style = "B")
        pdf.set_xy(x=X+60,y=Y)
        pdf.cell(w = 90,txt=f"{Q}")

        pdf.set_font("Arial",size = 15,style = "B")
        pdf.set_xy(x=X+90,y=Y)
        pdf.cell(w = 90,txt=f"{PU}")

        pdf.set_font("Arial",size = 15,style = "B")
        pdf.set_xy(x=X+120,y=Y)
        pdf.cell(w = 90,txt=f"{total}")
        
        Y = 200

        pdf.set_font("Courier",size = 11,style = "B")
        pdf.set_xy(x = X,y=Y)
        pdf.cell(w = 105,txt=f"!Bank Tips!")

        pdf.set_font("Courier",size  = 11)
        pdf.set_xy(x = X,y=Y+10)
        pdf.cell(w = 90,txt=f"Bank user is {BankU}")

        pdf.set_font("Courier",size  = 11)
        pdf.set_xy(x = X,y=Y+20)
        pdf.cell(w = 90,txt=f"Bank user is {BankP}")
        
        pdf.set_font("Courier",size  = 11)
        pdf.set_xy(x = X,y=Y+30)
        pdf.cell(w = 90,txt=f"Bank user is {BankN}")

        pdf.set_font("Arial",size  = 25)
        pdf.set_xy(x = 70,y=Y+10)
        pdf.cell(w = 120,txt=f"The total price is {total}AED")

        file_pdf= "invoice.pdf"
        pdf.output(file_pdf)
        return file_pdf
    
    pdf_func = generate_pdf()
    #read the pdf funct as binary data
    with open(pdf_func, 'rb') as binary:
        pdf_data = binary.read()

    st.write("this could take a moment")
    # if st.button("View Invoice"):
    #     if name and email and invoice and date and Ddate and D and Q and PU:
    #         #Write the PDF using base64
    #         pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')
    #         #Generate the HTML to embed the PDF
    #         pdf_embed = f'<embed src="data:application/pdf;base64,{pdf_base64}" type="application/pdf" width="100%" height="600px" />'
    #         #Display the embedded pdf (Markdown helps us use HTML in streamlit)
    #         st.markdown(pdf_embed,unsafe_allow_html=True)
    #     else:
    #         st.error("Sorry something isnt filled!")    


    if name and email and invoice and date and Ddate and D and Q and PU:
        st.download_button(label = "Download",data = pdf_data,file_name = f"Invoice{invoice}.pdf",
                           mime = "application/pdf")




######################################################################location edit    
else:
    st.title("Location Edit")
    st.write("")
    st.write("")
    Country = st.text_input("Enter Country")
    company = st.text_input("Enter Company")
    l,r=st.columns(2)
    with l:
        street= st.text_input("Enter Street")
        city = st.text_input("Enter City")
    with r:
        BankU = st.text_input("Enter bank username")
        BankP = st.text_input("Enter bank password")
    if st.button("Save"):

        st.success("save")