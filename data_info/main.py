from pages.processor.loading import loaded_data 
import streamlit as st

df = loaded_data() 


column_config = {
    
    "Age":st.column_config.BarChartColumn("Age",y_min=0,y_max=100)
}

st.data_editor(df,column_config=column_config)

