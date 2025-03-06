import pandas as pd
import os
import joblib

class preprocessing():
    def __init__(self):
        pass
    def data_preprocessing(self):
        df=pd.read_csv(r'C:\Users\HOME\Python-Jupyter\bootcamp feb25\data\cleaned_data\cleaned_data.csv')


        cat_col = df.select_dtypes(include='object').columns.to_list()

        # One-hot encoding
        df = pd.get_dummies(df, columns=cat_col, drop_first=True, dtype='int')
        joblib.dump(one_hot_encoding,r'C:\Users\HOME\Python-Jupyter\bootcamp feb25\models\one_hot_encoder')

        df.drop('StudentID',axis=1,inplace=True)

        os.makedirs(r'C:\Users\HOME\Python-Jupyter\bootcamp feb25\data\preprocess_data',exist_ok=True)
        df.to_csv(r'C:\Users\HOME\Python-Jupyter\bootcamp feb25\data\preprocess_data\preprocessed.csv',index= False)

if __name__=='__main__':
    try:
        obj = preprocessing()
        obj.data_preprocessing()
    except Exception as e:
        raise e