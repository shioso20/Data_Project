from loading import loaded_data 

df = loaded_data()


def menu_tab():

        print("=========================================================")

        print("1. Describe data ")

        print("2. Number of columns")

        print("3 Number of Rows")
        
        print("4. Exit")

        print("=========================================================")

        query = int(input("Select option [1-4]: "))
        
        


        if query == 1:
            
            print("Data Description:")
            print(df.describe())
            menu_tab()
            
        elif query == 2:
            
            print("Number of columns:")
            print(df.shape[1])
            menu_tab()
            
        elif query == 3:
            
            print("Number of rows:")
            print(df.shape[0])
            menu_tab()
            
        else: 
            
            print("Exiting...")
            exit()
            
menu_tab()