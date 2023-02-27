import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("car data.csv")
st.title("Plots in the our chart")
st.write("Data")
st.write(data)
st.write(data.isnull().sum())
st.write(data["Year"])
st.write(data.describe())
clist = data["Year"].unique().tolist()
Years = st.multiselect("Select Year", clist)
st.map()
# plt.plot(data["Year"],data["Selling_Price"])
fig, ax = plt.subplots()
plt.title("Line chart over the year")
ax.plot(data["Year"],data["Selling_Price"])
st.pyplot(fig)
st.title("This is My identity")
st.image("Image.jpg",width=500)