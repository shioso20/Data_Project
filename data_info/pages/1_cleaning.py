import streamlit as st 

from pages.processor.loading import loaded_data
from pages.processor.cleaning import DataCleaning
from pages.processor.rem_outliers import IQR

'''

Loads Initial file \n

'''

df = loaded_data()



st.header("Credit Risk Analysis")

st.sidebar.write("Links")

sub1,sub2 = st.columns(2)

sub1.subheader("Data Preprocessing")

'''

Auto save: \n

once turned on ; checks if session exists if not its creates and saves initial file \n

============================================================= \n
'''

auto_save  = sub1.toggle("Auto save on")

if auto_save: 
    
    sub1.info("Auto Save is on")
    
    if "cleaned_data_updated"  not in st.session_state: 
        
        st.session_state["cleaned_data_updated"] = df
        
        
    
else: 
    
    sub1.error("Auto Save is OFF:")
    
'''

ENDS Auto save processs \n

============================================================= \n
'''

'''

Processes Menu: \n

Radio button to select process to performs \n

============================================================= \n
'''

'''

1. Describes Data \n
2. Checks Nullity \n
3. Removes unwanted characters \n

============================================================= \n
'''

commands = sub1.radio("Function to Perform: ",["Describe Data","Check Nullity","Replace Unwanted Character","Remove Outliers"])

if commands == "Describe Data": 
    
    with st.spinner("please wait--"):
        df = DataCleaning(df,"").describe_data()
        
        

    
elif commands == "Check Nullity":
    
    col_to_check_nullity = sub1.selectbox("Select column to check nullity",df.columns) 
    
    sum_ = DataCleaning(df,col_to_check_nullity).check_nullity()
    
    sub2.write(sum_)
    
    
elif commands == "Replace Unwanted Character": 
    
    # variabled for columns to remove characters
    init_columns = sub1.multiselect("Select columns with unwanted char:",df.columns)
    
     # variabled for char(s) to replace sepeareted by space
    char_to_rem = sub1.text_input("Char to Rem: sep by space").split(" ")
    
    # variabled for char to replace with
    char_to_replace_with = sub1.text_input("Char to Rep With: ")
    
    # button to perform cleaning function
    clean_btn  = sub1.button("Replace")
    
    if clean_btn:
        
        # progress spinner
        with sub1.status("Done Cleaning..."):
            
          
                try:
                    
                    '''
                    ============================================ \n
                      checks if session exists : \n
                      NB :dataframe is saved in this session \n
                      
                      if exists df saved becomes the current df \n
                      if not the initial loeded data is cleaned and saved in session \n
                    '''
                    
                    if "cleaned_data_updated" in  st.session_state: 
                        
                        df = st.session_state["cleaned_data_updated"]
                        
                    
                    
                    df = DataCleaning(df,init_columns).rem_unwanted_char(char_to_rem,char_to_replace_with)
                    st.session_state["cleaned_data_updated"] = df
                    
                except Exception as e: 
                    
                    sub2.error(e)
                    
elif commands == "Remove Outliers": 
    
    rem_outlier_method = sub1.radio("Select Methos: ",["IQR","Z-SCORE"])
    
    if rem_outlier_method == "IQR": 
        
        col_rem_outlier = sub1.selectbox("Select Column",df.columns)
        
        if sub1.button("Remove Outliers"):
        
            
            
            
            if "cleaned_data_updated" in  st.session_state:
                
                df = st.session_state["cleaned_data_updated"]
                
            
            
            IQR_ = IQR(df,col_rem_outlier)
            
            Q1,Q2 = IQR_.calculate_all() 
            
            df = df[(df[col_rem_outlier] < Q2) & (df[col_rem_outlier] > Q1)]
            
            st.session_state["cleaned_data_updated"] = df
            
            
        
        
        
        
    
    
    
                
                
'''
======================================                                                                                                                                                                                         L
\n
display df: \n

checks if session exists: \n
if exists display the dataframe saved in session \n
if not initial loaded data is displayed. \n

'''       
if "cleaned_data_updated" in st.session_state:
    
    try:      
      
      df = st.session_state["cleaned_data_updated"]
      
      
      
    except Exception as err: 
        
        sub2.write(err)
  
sub2.dataframe(df)  
    
    




