import streamlit as st 
from loading import loaded_data

st.header("Credit Risk Analysis")

col = st.selectbox("Select one Column:",loaded_data().columns)

df = loaded_data()[col]

st.dataframe(df)

