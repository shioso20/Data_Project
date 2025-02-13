import streamlit as st 
import numpy as np
from pages.processor.info import describe_data,data_summary
from pages.processor.loading import loaded_data

st.subheader(" Summary Page ") 


# describe # calculate metrics # grouping 

col1,col2 = st.columns(2)


col1.dataframe(describe_data()) 

df = loaded_data()

grouper = st.sidebar.selectbox("groupby:",df.columns)

calculate = st.sidebar.selectbox("Calculate:",df.columns)

select_age = st.sidebar.slider("Start",20,60,(20,60))

st.write(select_age)


apply_button = st.sidebar.button("Apply")

if apply_button:

    params = data_summary(grouper = [grouper],agg = {calculate:[min,max,np.mean]},df=df)

    col2.dataframe(params)

   
    
else: 
    
    col2.info("Results appear here")