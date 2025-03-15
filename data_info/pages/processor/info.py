from pages.processor.loading import loaded_data
import numpy as np





def describe_data(df):

    return df.describe()


def data_summary(**kwargs): 
    
    
    new_group = kwargs["df"].groupby(kwargs["grouper"]).agg(kwargs["agg"])
    
    return new_group



    
    
    
    