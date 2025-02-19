
import streamlit as st 
from pages.processor.charts import  display_outliers
from pages.processor.loading import loaded_data




if "cleaned_data_updated" in  st.session_state:
    
    df = st.session_state["cleaned_data_updated"]
    
else:
    
    df = loaded_data()
    
col4_,col1_,col2_,col3_ = st.columns(4)

color = col4_.selectbox("Select Color:",["blue","green","orange","yellow"])
x_col = col1_.selectbox("Select X:",df.columns)
y_col = col2_.selectbox("Select Y:",df.columns)
hue_col = col3_.selectbox("Select Hue:",df.columns)

fig = display_outliers(df,x_col,y_col,hue_col,color)

st.pyplot(fig)