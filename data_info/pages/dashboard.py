
import streamlit as st 
from pages.processor.charts import  display_outliers
from pages.processor.loading import loaded_data
from pages.processor.state_manager import create_sess_state
from pages.processor.metrics import calculate_credit_risk,calculate_credit_risk_by_gender
import plotly.express as px
import pathlib





file = open("pages/page_style/style.css")

file = file.read()


st.markdown(f'<style>{file}</style>',unsafe_allow_html=True)

if "cleaned_data_updated" in  st.session_state:
    
    df = st.session_state["cleaned_data_updated"]
    
else:
    
    df = loaded_data()

col1,col2,col3,col4 = st.columns(4)
sub1,sub2 = st.columns(2)

low,high,ratio = calculate_credit_risk(df)
high_,low_,ratio_high,ratio_low = calculate_credit_risk_by_gender(df)

with col1: 
    
    with st.container(border=True,key="metric1"): 
        
        
        st.metric("Low Credit Risk",low,ratio)
        
with col2: 
    
    with st.container(border=True,key="metric2"): 
        
        st.metric("High Credit Risk",high,ratio)
        
with col3: 
    
    with st.container(border=True,key="metric3"): 
        
        st.metric("High Credit Risk Gender Ratio",high_,ratio_high)
        
with col4: 
    
    with st.container(border=True,key="metric4"): 
        
        st.metric("Low Credit Risk Gender Ratio",low_,ratio_low)
        
    
    


    
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
        
        
fig = px.line(df, x="Savings", y="Months Employed", color="Gender", hover_name="Gender",animation_frame="Age", animation_group="Gender",
        line_shape="spline", render_mode="svg")


with st.container(border=True):

    st.plotly_chart(fig)