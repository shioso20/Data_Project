from pages.processor.web_scraping import get_tables 
from pages.processor.state_manager import create_sess_state
import streamlit as st   


col1,col2 = st.columns((1,2))

if "scraped_table" in st.session_state: 
    
    if col2.button("Delete Session"): 
        
        del st.session_state["scraped_table"]
    
else: 
    
    col2.info("No Session")
    
    
url = col1.text_input("Page Url")
table_no = col1.text_input("table no")





if col1.button("Get Table"): 
    
    table = get_tables(url,int(table_no))
    
    if "scraped_table" not in st.session_state: 
        
        st.session_state["scraped_table"] = table 
        
        table  = st.session_state["scraped_table"]
        
    else: 
    
        table =  st.session_state["scraped_table"]
    
    
    with col2.container(border=True): 
        
      
        
        
            col2.data_editor(table)
            
            

if st.button("Pass to Cleaning"): 
    
    df = st.session_state["scraped_table"]
    
    create_sess_state("cleaned_data_updated",df)
    


