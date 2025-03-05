import pandas as pd
from sklearn.model_selection import RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import os
import joblib

class hyperparametertuning():
    def __init__(self):
        pass
    def hyperparameter_tuning(self):

        model = joblib.load(r'C:\Users\HOME\Python-Jupyter\bootcamp feb25\models\model')

        
        # Define hyperparameters for tuning
        param_grid = {
            'LogisticRegression()': {
                'C': [0.01, 0.1, 1, 10],
                'solver': ['liblinear', 'lbfgs']
            },
            'DecisionTreeClassifier(random_state=42)': {
                'max_depth': [3, 5, 10, None],
                'min_samples_split': [2, 5, 10]
            },
            'RandomForestClassifier(random_state=42)': {
                'n_estimators': [50, 100, 200],
                'max_depth': [None, 10, 20],
                'min_samples_split': [2, 5, 10]
            },
            'AdaBoostClassifier(random_state=42)': {
                'n_estimators': [50, 100, 200],
                'learning_rate': [0.01, 0.1, 1]
            },
            'GradientBoostingClassifier(random_state=42)': {
                'n_estimators': [50, 100, 200],
                'learning_rate': [0.01, 0.1, 0.2],
                'max_depth': [3, 5, 10]
            }
        }

        param_grid = param_grid[str(model)]

        df=pd.read_csv(r'C:\Users\HOME\Python-Jupyter\bootcamp feb25\data\preprocess_data\preprocessed.csv')

        X = df.drop(columns=["PlacementStatus_Placed"])
        y = df["PlacementStatus_Placed"]

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        X_train, X_test, y_train, y_test = train_test_split(X_scaled,y,test_size = 0.2)

        random_search = RandomizedSearchCV(
        estimator=model,
        param_distributions= param_grid,
        cv = 5,
        scoring='accuracy',
        n_jobs=-1,
        random_state=42
        )

        random_search.fit(X_train,y_train)

        print(f'Best Parameters for {model}: {random_search.best_params_}')
        print(f"Best Score: {random_search.best_score_}")

        


if __name__=='__main__':
    try:
        obj = hyperparametertuning()
        obj.hyperparameter_tuning()
    except Exception as e:
        raise e