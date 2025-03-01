import streamlit as st 
import numpy as np
from pages.processor.info import describe_data,data_summary
from pages.processor.loading import loaded_data


st.subheader(" Summary Page ") 

'''

============================\n
displays all session states

'''

if st.session_state: 
    st.write("Available sessions")
    
    st.write(st.session_state)
# describe # calculate metrics # grouping 

col1,col2 = st.columns(2)


with col1: 
    
    with st.container(border=True,height=400):

        st.dataframe(describe_data())

'''
===============================\n
if there is any df in session \n
its used as current: \n
if not the initial loaded data is used.

''' 

if "cleaned_data_updated" in st.session_state: 
    
    df = st.session_state["cleaned_data_updated"]
    
else: 
    

     df = loaded_data()
     

'''
============================
grouping data: \n
creates summary\n

'''
grouper = st.sidebar.selectbox("groupby:",df.columns)

calculate = st.sidebar.selectbox("Calculate:",df.columns)

select_age = st.sidebar.slider("Select Age Group",20,60,(20,60))




apply_button = st.sidebar.button("Apply")

if apply_button:
    
    df = df[(df["Age"] >= select_age[0]) & (df["Age"] <= select_age[1]) ]

    params = data_summary(grouper = [grouper],agg = {calculate:[min,max,np.mean]},df=df)
    
    with col2: 
    
        with st.container(border=True,height=400):

            st.dataframe(params)

   
    
else: 
    
    col2.info("Results appear here")