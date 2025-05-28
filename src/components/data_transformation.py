import sys
import os
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformaton_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation.
        '''
        try:
            numerical_columns=["reading_score", "writing_score"]
            categorical_columns = [
                "gender", "race_ethnicity", "parental_level_of_education", "lunch", "test_preparation_course"
            ]
            num_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")), #handles missing values
                    ("scaler",StandardScaler()) # does scaling numerical values
                ]
            )
            cat_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")), #handles missing values
                    ("one_hot_encoder",OneHotEncoder()), # does one hot encoding of Categorical columns
                    ("scaler", StandardScaler(with_mean=False))  # trust me - even i could not get why i am doing with_mean = False. Chatgpt tells me that OHE produces a sparse matrix and we can not center that sparse data using StandardScaler. God knows why.
                ]
            )
            
            logging.info("Categorical columns Standard Scaling completed.")
            logging.info("categorical columns encoding completed.")
            
            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_columns),
                    ("cat_pipeline",cat_pipeline,categorical_columns)
                ]
            )
            
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logging.info("Read Train and Test data completed.")
            logging.info("Obtaining pre-processing object.")
            
            preprocessing_obj = self.get_data_transformer_object()
            target_column_name = "math_score"
            numerical_columns=["reading_score", "writing_score"]

            input_feature_train_df = train_df.drop(columns=[target_column_name], axis = 1)
            target_feature_train = train_df[target_column_name]
            input_feature_test = test_df.drop(columns=[target_column_name], axis = 1)
            target_feature_test = test_df[target_column_name]
            
            logging.info("Applying preprocessor object on training dataframe and testing dataframe")
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test)        
            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train)
            ]

            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test)]
            logging.info("Saving pre-processed object")

            save_object(file_path = self.data_transformaton_config.preprocessor_obj_file_path, obj = preprocessing_obj)
            return (
                train_arr, test_arr, self.data_transformaton_config.preprocessor_obj_file_path
            )
        except Exception as e:
            raise CustomException(e,sys)