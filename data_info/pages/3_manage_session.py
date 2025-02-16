import streamlit as st

'''

display all session states saved 
button to deleted each session

'''
 
col1,col2,col3 = st.columns(3)

results = []

for key in st.session_state.keys(): 
    
    col1.write(key)
    
    if col2.button("delete"): 
        
        results.append("Deleted: "+str(st.session_state[key]))
        
        del st.session_state[key]
        
        
        
        
for result in results: 
    
    st.write(result)
    
    
    

    