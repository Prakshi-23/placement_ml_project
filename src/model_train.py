import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import os
import joblib

class model_train():
    def __init__(self):
        pass
    def model_training(self):
        df=pd.read_csv(r'C:\Users\HOME\Python-Jupyter\bootcamp_feb25\data\preprocess_data\preprocessed.csv')
        X = df.drop(columns=["PlacementStatus_Placed"])
        y = df["PlacementStatus_Placed"]


        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        joblib.dump(scaler,r'C:\Users\HOME\Python-Jupyter\bootcamp_feb25\models\scaler')

        X_train, X_test, y_train, y_test = train_test_split(X_scaled,y,test_size = 0.2)

        models = [LogisticRegression(), DecisionTreeClassifier(random_state=42), 
          RandomForestClassifier(random_state=42),
          AdaBoostClassifier(random_state=42),GradientBoostingClassifier(random_state=42)]
        
        d = {}
        for i in models:
            i.fit(X_train,y_train)
            pred = i.predict(X_test)
            acc = accuracy_score(y_test, pred)
            if acc not in d:
                d[i] = acc

        model = [a for a,b in d.items() if b == max(d.values())][0]

       
        os.makedirs(r'C:\Users\HOME\Python-Jupyter\bootcamp_feb25\models',exist_ok=True)

        joblib.dump(model,r'C:\Users\HOME\Python-Jupyter\bootcamp_feb25\models\model')

if __name__=='__main__':
    try:
        obj = model_train()
        obj.model_training()
    except Exception as e:
        raise e