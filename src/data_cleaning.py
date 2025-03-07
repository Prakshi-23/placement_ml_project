import pandas as pd
import os

class datacleaning():
    def __init__(self):
        pass
    def data_cleaning(self):
        df = pd.read_csv(r'C:\Users\HOME\Python-Jupyter\bootcamp_feb25\data\raw_data\raw.csv')
        df.info()
        df.describe()
        df.duplicated().sum()
        df.isnull().sum()

        os.makedirs(r'C:\Users\HOME\Python-Jupyter\bootcamp_feb25\data\cleaned_data',exist_ok=True)
        df.to_csv(r'C:\Users\HOME\Python-Jupyter\bootcamp_feb25\data\cleaned_data\cleaned_data.csv',index=False)

if __name__=='__main__':
    try:
        obj = datacleaning()
        obj.data_cleaning()
    except Exception as e:
        raise e
    

#  no print statements should be copied