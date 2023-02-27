import streamlit as st
st.write("Welcome to My load_data streamlit ")
d={"sanju":92,"rohan":23}
st.write(d)
import pandas as pd
import numpy as np
data=pd.read_csv("car data.csv")
st.write(data)
# st.dataframe(data)
st.dataframe(d)
st.table(d)