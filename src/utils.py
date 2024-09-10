import os, sys
import pandas as pd
import numpy as np
import dill
import pickle

from src.exception import CustomException
from src.logger import logging

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path, data):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(data, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    


def evaluate_model(X_train, y_train, X_test, y_test, models, params):
    
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = params[list(models.keys())[i]]
            
            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)
            
            y_test_predict = model.predict(X_test)
            test_model_score = r2_score(y_test, y_test_predict)
            report[list(models.keys())[i]] = test_model_score
        return report
    
    except Exception as e:
        raise CustomException(e,sys)
    

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)