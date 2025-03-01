
import streamlit as st 
from pages.processor.charts import  display_outliers
from pages.processor.loading import loaded_data
from pages.processor.state_manager import create_sess_state
import pathlib


def load_style(path):

    with open(path) as file:

        st.html(f'<style>{file}</style>')


style_path = pathlib.Path("pages/page_style/style.css")

load_style(style_path)


sub1,sub2 = st.columns(2)

if "cleaned_data_updated" in  st.session_state:
    
    df = st.session_state["cleaned_data_updated"]
    
else:
    
    df = loaded_data()
    
chart_type = st.sidebar.selectbox("Chart Type to Change",["All","line","bar"])
if chart_type == "All":
    color = st.sidebar.selectbox("Select Color:",["blue","green","orange","yellow"])
    x_col = st.sidebar.selectbox("Select X:",df.columns)
    y_col = st.sidebar.selectbox("Select Y:",df.columns)
    hue_col = st.sidebar.color_picker("Select Color")
    
    
    create_sess_state("line",[x_col,y_col]) 
    create_sess_state("bar",[x_col,y_col]) 
    
    x_bar_col,y_bar_col = st.session_state["bar"][0],st.session_state["bar"][1]
    
    x_line_col,y_line_col = st.session_state["line"][0],st.session_state["line"][1]
    
    

elif chart_type == "line": 
    
    color = st.sidebar.selectbox("Select Color:",["blue","green","orange","yellow"])
    x_line_col = st.sidebar.selectbox("Select X:",df.columns)
    y_line_col = st.sidebar.selectbox("Select Y:",df.columns)
    hue_col = st.sidebar.color_picker("Select Color")
    
    x_bar_col,y_bar_col = st.session_state["bar"][0],st.session_state["bar"][1]
    x_line_col,y_line_col = x_line_col,y_line_col
    
    st.session_state["line"] = [x_line_col,y_line_col]
    
    
elif chart_type == "bar": 
    
    color = st.sidebar.selectbox("Select Color:",["blue","green","orange","yellow"])
    x_bar_col = st.sidebar.selectbox("Select X:",df.columns)
    y_bar_col = st.sidebar.selectbox("Select Y:",df.columns)
    hue_col = st.sidebar.color_picker("Select Color")
    
    x_bar_col,y_bar_col = x_bar_col,y_bar_col
    x_line_col,y_line_col = st.session_state["line"][0],st.session_state["line"][1]
    
    st.session_state["bar"] = [x_bar_col,y_bar_col]
    

with sub1:
    with st.container(border=True,key="bars"):
        st.bar_chart(df,x=x_bar_col,y=y_bar_col)

with sub2:
    
    with st.container(border=True,key="line"):
        st.line_chart(df,x=x_line_col,y=y_line_col,color=hue_col)