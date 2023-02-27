import streamlit as st
import pandas as pd

## set the page configuration using this command
st.set_page_config(page_title="My Streamlit Practice",page_icon=":smiley:")

#title
st.title("India is my country and this is in the Title keyword in streamlit")

#text
st.text("This is text what we write in the streamlit")

#Header 

st.header("this is for write the header")

#subheader
st.subheader("This is write with help of subheader in streamlit")


## now there are some keuwords by using these keywords we can use some color part of that perticular line

st.success("Wow finally my model is deployed and using by success ")
st.warning("This will also show warning color")
st.info("This will show also some color according to info")
st.error("This will show some color according to error")
st.exception(RuntimeError("This is also used for the show the color using expection cases")) # for expection we have to give some error


##use of streamlit for see the data
# st.write("This is My data")
st.dataframe(pd.read_csv("car data.csv"))

##button
if st.button("Submit"):
    st.write("Hello it is only for checking the button")

# as we want more than one button in our app we need to give some different key to each button
if st.button("Submit",key="01"):
    st.write("This is my second submit button")

##Radio button

status=st.radio("what is your status",("active","inactive"))
if status=="active":
    st.write("You are active now")
else:
    st.write("you not active now")

##checkbox
if st.checkbox("show/Hide"):
    st.write("This is what is hide inside into the checkbox")

##expander
with st.expander("Expand for show the more about streamlit"):
    st.write("there are many keywords which just need to remeber in streamlit web application creation")


##select Box
l=["Python","java","c++","c"]
s_language=st.selectbox("Select one Language ",l)
for i in l:
    if s_language==i:
        st.info(f"you select the {i} Language.. ")

##Multiselect Box
l1=["Python","java","c++","c"]
sm_language=st.multiselect("Select Mulitple Language ",l1)

##slider 
st.slider("Select the Age range",1,100)

##Reading the Image by using streamlit
from PIL import Image
img=Image.open("Image.jpg")
st.image(img)
st.image(img,use_column_width=True)

st.date_input("Input you birthday date")

##some ploting using plotly
import plotly.express as epz
data=pd.read_csv("car data.csv")
st.dataframe(data.head(2))
fig=epz.line(data["Year"],data["Selling_Price"])
st.plotly_chart(fig)

##creating bar chart using plotly
fig2=epz.bar(data["Seller_Type"],data["Selling_Price"])
st.plotly_chart(fig2)

fig3=epz.pie(values=data["Selling_Price"],names=data["Seller_Type"])
st.plotly_chart(fig3)







