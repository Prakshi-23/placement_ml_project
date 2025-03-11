
## Overview
This project is an end-to-end machine learning solution for predicting student placements. It involves data collection, preprocessing, model training, hyperparameter tuning, and deployment using Streamlit.

## Project Structure
```
├── data
│   ├── raw_data
│   │   ├── raw.csv
│   ├── cleaned_data
│   ├── preprocess_data
├── models
│   ├── best_model
│   ├── model
│   ├── scaler
├── notebooks
│   ├── data_collection.ipynb
│   ├── data_cleaning.ipynb
│   ├── preprocessing.ipynb
│   ├── model_train.ipynb
│   ├── hyperparameter_tuning.ipynb
├── src
│   ├── data_collection.py
│   ├── data_cleaning.py
│   ├── preprocessing.py
│   ├── model_train.py
│   ├── hyperparameter_tuning.py
│   ├── app.py
│   ├── main.py
│   ├── streamlit.py
│   ├── test.py
│   ├── requirements.txt
├── placementdata.csv
├── .gitignore
```

## Pipeline Steps
### 1. Data Collection
- The raw dataset (`raw.csv`) is gathered and stored in the `data/raw_data/` directory.
- The `data_collection.ipynb` and `data_collection.py` scripts are used to fetch and save the data.

### 2. Data Cleaning
- Missing values, duplicate records, and irrelevant features are handled.
- The cleaned data is stored in the `data/cleaned_data/` directory.
- Implemented in `data_cleaning.ipynb` and `data_cleaning.py`.

### 3. Data Preprocessing
- Feature engineering, encoding categorical variables, and feature scaling.
- Preprocessed data is saved in `data/preprocess_data/`.
- Implemented in `preprocessing.ipynb` and `preprocessing.py`.

### 4. Model Training
- Multiple classification models were trained:
  - **Logistic Regression**: 79.8%
  - **Decision Tree Classifier**: 71.25%
  - **Random Forest Classifier**: 79.1%
  - **AdaBoost Classifier**: 81.05% (Best Model)
  - **Gradient Boosting Classifier**: 80.3%
- Implemented in `model_train.ipynb` and `model_train.py`.
- Trained models are saved in the `models/model/` directory.

### 5. Hyperparameter Tuning
- Models are optimized to improve accuracy.
- The best-performing model (AdaBoost) is saved in `models/best_model/`.
- Implemented in `hyperparameter_tuning.ipynb` and `hyperparameter_tuning.py`.

### 6. Model Deployment
- The best model is used for predictions.
- A **Streamlit** web application is created for user interaction.
- Implemented in `app.py` and `streamlit.py`.

### 7. Testing and Evaluation
- The final model is evaluated on test data.
- Results and metrics are logged.
- Implemented in `test.py`.

## Installation and Usage
### Requirements
Install dependencies using:
```
pip install -r requirements.txt
```

### Running the App
Run the Streamlit app with:
```
streamlit run app.py
```

## Future Improvements
- Improve model accuracy with additional feature engineering.
- Integrate a database for real-time student placement tracking.
- Expand deployment options using Flask/Django for a web-based solution.

## Author
Prakshi Karkera
