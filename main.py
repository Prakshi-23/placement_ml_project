from src.data_collection import datacollection

try:
    obj = datacollection()
    obj.data_collection()
    print("Stage data collection completed successfully")
except Exception as e:
    raise e

from src.data_cleaning import datacleaning

try:
    obj = datacleaning()
    obj.data_cleaning()
    print("Stage data cleaning completed successfully")
except Exception as e:
    raise e

from src.preprocessing import preprocessing

try:
    obj = preprocessing()
    obj.data_preprocessing()
    print("Stage data preprocessing completed successfully")
except Exception as e:
    raise e


from src.model_train import model_train

try:
    obj = model_train()
    obj.model_training()
    print("Stage model training completed successfully")
except Exception as e:
    raise e


from src.hyperparameter_tuning import hyperparametertuning

try:
    obj = hyperparametertuning()
    obj.hyperparameter_tuning()
    print("Stage hyperparameter tuning completed successfully")
except Exception as e:
    raise e