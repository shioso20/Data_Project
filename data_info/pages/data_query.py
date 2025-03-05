import streamlit as st 
from pages.processor.ai_query import chat_msg 
from pages.processor.state_manager import create_sess_state



st.header("Data Query")

create_sess_state("cleaned_data_updated","")

prompt_ = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello"},
        

    ]


prompt = st.chat_input( 
             
             "Query here" ,
                
                       
                       )



if prompt:
    
    prompt_.append(
        
        {"role": "user", "content": prompt}
    )
    
    reply = chat_msg(prompt)
    
    
   
    with st.container(border=True):
        
        st.write_stream(reply)