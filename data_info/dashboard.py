import streamlit as st 
from loading import loaded_data
from cleaning import DataCleaning

df = loaded_data()

st.header("Credit Risk Analysis")

st.sidebar.write("Links")

sub1,sub2 = st.columns(2)

sub1.subheader("Data Preprocessing")

auto_save  = sub1.toggle("Auto save on")

if auto_save: 
    
    sub1.info("Auto Save is on")
    
else: 
    
    sub1.error("Auto Save is OFF:")

commands = sub1.radio("Function to Perform: ",["Describe Data","Check Nullity","Replace Unwanted Character"])

if commands == "Describe Data": 
    
    df = DataCleaning(df,"").describe_data()
    

elif commands == "Check Nullity":
    
    col_to_check_nullity = sub1.selectbox("Select column to check nullity",df.columns) 
    
    sum_ = DataCleaning(df,col_to_check_nullity).check_nullity()
    
    sub2.write(sum_)
    
    
elif commands == "Replace Unwanted Character": 
    
    init_columns = sub1.multiselect("Select columns with unwanted char:",df.columns)
    
    char_to_rem = sub1.text_input("Char to Rem: ")
    
    char_to_replace_with = sub1.text_input("Char to Rep With: ")
    
    df = DataCleaning(df,init_columns).rem_unwanted_char([char_to_rem],char_to_replace_with)
    
    

sub2.dataframe(df)

df.to_csv("temp.csv")


