import streamlit as st 

from pages.processor.loading import loaded_data
from pages.processor.cleaning import DataCleaning,DataReshaping
from pages.processor.rem_outliers import IQR
from pages.processor.state_manager import create_sess_state,del_sess_state
from pages.processor.encoding import label_encoding,one_hot_encoding



df = loaded_data()



st.header("Credit Risk Analysis")

st.sidebar.write("Links")

sub1,sub2 = st.columns([3,1])

sub1.subheader("Data Preprocessing")

if sub2.button("Delete Session"):
    del_sess_state("cleaned_data_updated",sub2)

sub1.divider()
sub2.divider()

auto_save  = st.sidebar.toggle("Auto save on")

if auto_save: 
    
    st.sidebar.info("Auto Save is on")
      
    create_sess_state("cleaned_data_updated",df)
    create_sess_state("reshaped_data","")
    
    
        
        
    
else: 
    
    sub1.error("Auto Save is OFF:")
    


commands = sub1.radio("Function to Perform: ",["Describe Data","Check Nullity","Replace Character","Remove Outliers","Reshaping Data","Encode Data"],horizontal=True)

if commands == "Describe Data": 
    
    with st.spinner("please wait--"):
        df = DataCleaning(df,"").describe_data()
        
        

    
elif commands == "Check Nullity":
    
    col_to_check_nullity = sub2.selectbox("Select column to check nullity",df.columns) 
    
    sum_ = DataCleaning(df,col_to_check_nullity).check_nullity()
    
    sub2.write(sum_)
    
    
elif commands == "Replace Character": 
    
    # variabled for columns to remove characters
    init_columns = sub2.multiselect("Select columns with unwanted char:",df.columns)
    
     # variabled for char(s) to replace sepeareted by space
    char_to_rem = sub2.text_input("Char to Rem: sep by space").split(" ")
    
    # variabled for char to replace with
    char_to_replace_with = sub2.text_input("Char to Rep With: ")
    
    # button to perform cleaning function
    clean_btn  = sub2.button("Replace")
    
    if clean_btn:
        
        # progress spinner
        with sub2.status("Done Cleaning..."):
            
          
                try:
                    
                    
                    
                    if "cleaned_data_updated" in  st.session_state: 
                        
                        df = st.session_state["cleaned_data_updated"]
                        
                    
                    
                    df = DataCleaning(df,init_columns).rem_unwanted_char(char_to_rem,char_to_replace_with)
                    st.session_state["cleaned_data_updated"] = df
                    
                except Exception as e: 
                    
                    sub2.error(e)
                    
elif commands == "Remove Outliers": 
    
    rem_outlier_method = sub2.radio("Select Methos: ",["IQR","Z-SCORE"])
    
    if rem_outlier_method == "IQR": 
        
        col_rem_outlier = sub2.selectbox("Select Column",df.columns)
        
        if sub2.button("Remove Outliers"):
        
            
            
            
            if "cleaned_data_updated" in  st.session_state:
                
                df = st.session_state["cleaned_data_updated"]
                
            
            
            IQR_ = IQR(df,col_rem_outlier)
            
            Q1,Q2 = IQR_.calculate_all() 
            
            df = df[(df[col_rem_outlier] < Q2) & (df[col_rem_outlier] > Q1)]
            
            st.session_state["cleaned_data_updated"] = df
            
            
elif commands == "Reshaping Data": 
    
    reshaping_opt = sub2.radio("Select Reshaping Option: ",["Stack","Unstack","Melt"])
    
    
    
    if reshaping_opt == "Stack": 
        
        reshaping_method = DataReshaping(df,"",[],"")
        
        reshaped_df = reshaping_method.stack_df()
    
    elif reshaping_opt == "Unstack": 
        
        reshaping_method = DataReshaping(df,"",[],"")
        reshaped_df = reshaping_method.unstack_df()
    
    elif reshaping_opt == "Melt": 
        
        id_var = sub2.selectbox("Select Id Var:",df.columns)
        value_vars = sub2.multiselect("Select Id Var:",df.columns)
        attribute = "Attribute"
        
        reshaping_method = DataReshaping(df,id_var,value_vars,attribute)
        
        reshaped_df = reshaping_method.melt_df()
        
    if "reshaped_data" not in st.session_state: 
        
        create_sess_state("reshaped_data",reshaped_df) 
        
    st.session_state["reshaped_data"] = reshaped_df
    

elif commands == "Encode Data": 
    
    
     encoding_opt = sub2.radio("Select Encoding Option: ",["Label Encoding","One Hot"])
     
     sel_col_to_encode = sub2.selectbox("Select column to Encode: ",df.columns)
     
     if encoding_opt == "Label Encoding": 
         
         new_col_name = sub2.text_input("New column name") 
         
         if sub2.button("Label Encode"): 
             
             if "cleaned_data_updated" in st.session_state: 
                 
                df = st.session_state["cleaned_data_updated"] 
                
             df = label_encoding(df, sel_col_to_encode,new_col_name)
             
             st.session_state["cleaned_data_updated"] = df
            
         
         
     
     elif encoding_opt == "One Hot": 
         
         if sub2.button("One Hot Encode"):
         
            if "cleaned_data_updated" in st.session_state:
                
                df = st.session_state["cleaned_data_updated"] 
                
            df = one_hot_encoding(df,sel_col_to_encode,int)
            
            st.session_state["cleaned_data_updated"] = df
         
         
    
    
    
            
            
        
        
        
        
    
    
    
                
                
     

sub1.divider()

sub1.write("Cleaned Data")

sub2.write("Reshaped Data")

if "reshaped_data" in st.session_state:
    
    try:      
      
      reshaped_df = st.session_state["reshaped_data"]
      
      
      
    except Exception as err: 
        
        sub1.write(err)
        

        
        
if "cleaned_data_updated" in st.session_state:
    
    try:      
      
      df = st.session_state["cleaned_data_updated"]
      
      
      
    except Exception as err: 
        
        sub2.write(err)
  

st.dataframe(df) 

try: 
    
    st.dataframe(reshaped_df)  
    
except Exception as err: 
    
    st.write("DataFrame not Created")
    
    




