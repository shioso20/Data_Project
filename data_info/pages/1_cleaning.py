import streamlit as st 

from pages.processor.loading import loaded_data
from pages.processor.cleaning import DataCleaning

'''

Loads Initial file

'''

df = loaded_data()



st.header("Credit Risk Analysis")

st.sidebar.write("Links")

sub1,sub2 = st.columns(2)

sub1.subheader("Data Preprocessing")

'''

Auto save: 

once turned on ; checks if session exists if not its creates and saves initial file

=============================================================
'''

auto_save  = sub1.toggle("Auto save on")

if auto_save: 
    
    sub1.info("Auto Save is on")
    
    if "cleaned_data_updated"  not in st.session_state: 
        
        st.session_state["cleaned_data_updated"] = df
        
        
    
else: 
    
    sub1.error("Auto Save is OFF:")
    
'''

ENDS Auto save processs

=============================================================
'''

'''

Processes Menu: 

Radio button to select process to performs

=============================================================
'''

'''

1. Describes Data
2. Checks Nullity
3. Removes unwanted characters

=============================================================
'''

commands = sub1.radio("Function to Perform: ",["Describe Data","Check Nullity","Replace Unwanted Character"])

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
                    ============================================
                      checks if session exists : 
                      NB :dataframe is saved in this session 
                      
                      if exists df saved becomes the current df
                      if not the initial loeded data is cleaned and saved in session
                    '''
                    
                    if "cleaned_data_updated" in  st.session_state: 
                        
                        df = st.session_state["cleaned_data_updated"]
                        
                    
                    
                    df = DataCleaning(df,init_columns).rem_unwanted_char(char_to_rem,char_to_replace_with)
                    st.session_state["cleaned_data_updated"] = df
                    
                except Exception as e: 
                    
                    sub2.error(e)
                
                
'''
======================================
display df: 

checks if session exists: 
if exists display the dataframe saved in session
if not initial loaded data is displayed.

'''       
if "cleaned_data_updated" in st.session_state:
    
    try:      
      
      df = st.session_state["cleaned_data_updated"]
      
      
      
    except Exception as err: 
        
        sub2.write(err)
  
sub2.dataframe(df)  
    
    




