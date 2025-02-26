import streamlit as st

def create_sess_state(state_key,state_val): 
    
    if state_key not in st.session_state:  
        
        st.session_state[state_key]  = state_val 
        
    

def del_sess_state(state_key,sub): 
    
    if state_key in st.session_state: 
    
    
        del st.session_state[state_key]
        
        sub.warning("Session "+str(state_key)+" Deleted")
        
    else:  
    
         sub.error("Session "+str(state_key)+" does not Exists !!")
        
        
