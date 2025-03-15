import pandas as pd
from bs4 import BeautifulSoup as bs
from datetime import datetime
import requests
import time
import matplotlib.animation as animation 
import matplotlib.pyplot as plt

def get_tables(url,table_no): 
    
    html_ = pd.read_html(url)
    
    df = html_[table_no] 
    
    return df  


def scrap_web_elements(pair):
    
    url = "https://www.google.com/finance/quote/"+str(pair)
    
    resp = requests.get(url)
    
    html_ = bs(resp.content,'html.parser') 
    
    data = html_.find_all('div',{'class':'YMlKec fxKbKc'})
    
    return float(data[0].text.replace("$","")),datetime.now().strftime("%H:%M:%S")

    

fig, ax = plt.subplots()
x_,y_ = [],[]

def animate(i): 
    
   
    
    y,x = scrap_web_elements("TSLA:NASDAQ")
    
    
    
    
    x_.append(x)
    y_.append(y)
    
    ax.clear()
    ax.plot(x_,y_,marker="o", linestyle="-", color="b")
    
    ax.grid(True)
    
    
    

anim= animation.FuncAnimation(fig,animate,interval=1000)
plt.show()
    
    
    
    
    
