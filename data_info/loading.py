import pandas 
import os 

def get_filenames(path): 
    
    return [file for file in os.listdir(path)]
    
def loading_data(file):
    
    df = pandas.read_csv(file)
    
    return df

def loaded_data(): 

    path = r'C:\Users\EliteBook 800 G4\Videos\DataProjects\Data_Project\Data'

    file_name = get_filenames(path)

    full_path = os.path.join(path, file_name[0])

    return loading_data(full_path)
    
    
   