class DataCleaning: 
    
    
    def __init__(self,df,col): 
        
        self.df = df 
        self.col = col
        
    def describe_data(self): 
        
        return self.df.describe()
    
    def check_nullity(self): 
        
        return self.df[self.col].isnull().sum()
    
    def rem_unwanted_char(self,char_list,replace_by):
        
        for col in self.col:

            for char in char_list: 
            
                self.df[col] = self.df[col].str.replace(char,replace_by)
                
        return self.df 
    
    
    def assign_value(self,new_col): 
    
        
        category_label = {} 
        
        unique_values  = [val for val in self.df[self.col].unique()]
        
        print(unique_values)
        
        no_categories = len(unique_values)
        
        for i in range(no_categories):
            
            category_label[unique_values[i]] = i
            
        
        new_values = []
        
        for i in self.df[self.col]:
            
            for key,val in category_label.items():
                

                if i == key:
                
                    i = category_label[key] 
                    
                    new_values.append(i)
        
        self.df[new_col]   = new_values
            
        return self.df
    
    
    
    
    
    
            
            
            
            
            
            
    
    
    
    
