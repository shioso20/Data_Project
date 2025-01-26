import pandas 
import os 

def get_filenames(path): 
    
    return [file for file in os.listdir(path)]
    
def loading_data(file):
    

    """
    Load a CSV file into a pandas DataFrame.

    Parameters
    ----------
    file : str
        The path to the CSV file.

    Returns
    -------
    df : pandas.DataFrame
        The loaded data.
    """

    df = pandas.read_csv(file)
    
    return df



def loaded_data(): 


    """
    Load the first file in the specified path into a pandas DataFrame.

    Parameters
    ----------
    None

    Returns
    -------
    df : pandas.DataFrame
        The loaded data.

    """

    path = r'C:\Users\EliteBook 800 G4\Videos\DataProjects\Data_Project\Data'

    file_name = get_filenames(path)

    full_path = os.path.join(path, file_name[0])

    return loading_data(full_path)
    
    
   