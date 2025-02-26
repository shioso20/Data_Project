import pandas as pd
def label_encoding(data,col,new_col): 
    
    category_label = {} 
    
    unique_values  = [val for val in data[col].unique()]
    
    print(unique_values)
    
    no_categories = len(unique_values)
    
    for i in range(no_categories):
        
        category_label[unique_values[i]] = i
        
    
    new_values = []
    
    for i in data[col]:
        
        for key,val in category_label.items():
            

            if i == key:
            
                 i = category_label[key] 
                 
                 new_values.append(i)
     
    data[new_col]   = new_values
        
    return data


def one_hot_encoding(df,col,dtype): 
    
    return pd.get_dummies(df,columns=col,dtype=dtype)
    
    