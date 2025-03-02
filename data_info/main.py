from pages.processor.loading import loaded_data 
import streamlit as st 
import pathlib
import streamlit as st
st.set_page_config(layout="wide")

df = loaded_data() 

def load_style(path):

    with open(path) as file:

        st.html(f'<style>{file}</style>')


style_path = pathlib.Path("pages/page_style/style.css")

load_style(style_path)


dashboard_page = st.Page( 
                         
            page="pages/dashboard.py",
            title="Dashboard",
            icon=":material/dashboard:",
            default=True,
            
                         
                         
)

cleaning_page = st.Page( 
                         
            page="pages/cleaning.py",
            title="Data Cleaning",
            icon=":material/brush:",
          
                         
                         
)

summary_page = st.Page( 
                         
            page="pages/summary.py",
            title="Summarize Data",
            icon=":material/summarize:",
          
                         
                         
)

session_page = st.Page(
    
    page="pages/manage_sessions.py",
    title = "Session Manager",
    icon = ":material/settings:"
    
)

pg = st.navigation(
    
    {
                   
                   "Charts":[dashboard_page],
                   
                  "processess": [cleaning_page,summary_page],
                  
                  "Manage":[session_page]
                  
    }
                  
                  
                  )

pg.run()