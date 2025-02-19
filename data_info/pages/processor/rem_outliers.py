
class IQR: 
    
    def __init__(self,df,col): 
        
        self.df = df  
        self.col = col  
        
    def sort_list(self):  
        
        sorted_list = [val for val in self.df[self.col]]
        
        sorted_list.sort()
        
        return sorted_list
    
    def get_len(self,col): 
        
        return len([val for val in col]) 
        
    def split_col(self):
        
        n = self.get_len(self.df[self.col])
        
        if n % 2 == 0: 
            
            lower = self.sort_list()[:n//2-1]
            
            upper = self.sort_list()[n//2+1:n]
        
        elif n % 2 != 0: 
            
            
            lower = self.sort_list()[:n//2]
            upper = self.sort_list()[n//2+1:n]
            
        return lower,upper
        
    
    def calculate_odd_median(self,col):
        
        n = self.get_len(col)
        
        return col[n//2+1] 
    
    def calculate_even_median(self,col): 
        
        n = self.get_len(col)
        
        return sum(col[n//2:n//2+2])/2
    
    
    def check_odd_or_even(self,col):  
        
        n = self.get_len(col)
        
        if n % 2 == 0: 
            
            median = self.calculate_even_median(col)
        
        elif n % 2 != 0: 
            
            
            median = self.calculate_odd_median(col)
            
        return median
    
    
    def calculate_all(self): 
        
        lower ,upper = self.split_col()
        
        q1 = self.check_odd_or_even(lower)
        q2 = self.check_odd_or_even(upper)
        
        return q1,q2
        
        


