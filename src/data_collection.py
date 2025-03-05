import pandas as pd
import os 


class datacollection():
    def __init__(self):
        pass
    def data_collection(self):
        df = pd.read_csv(r'C:\Users\HOME\Python-Jupyter\bootcamp feb25\placementdata.csv')

        os.makedirs(r'C:\Users\HOME\Python-Jupyter\bootcamp feb25\data\raw_data',exist_ok=True)
        df.to_csv(r'C:\Users\HOME\Python-Jupyter\bootcamp feb25\data\raw_data\raw.csv',index= False)

if __name__=='__main__':
    try:
        obj = datacollection()
        obj.data_collection()
    except Exception as e:
        raise e
