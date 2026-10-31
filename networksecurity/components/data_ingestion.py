from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact

import os
import sys
import pymongo
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")


class DataIngestion:

    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config

            if not MONGO_DB_URL:
                raise ValueError("MONGO_DB_URL is missing")

        except Exception as e:
            raise NetworkSecurityException(e, sys) from e

    def export_collection_as_dataframe(self):
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name

            mongo_client = pymongo.MongoClient(MONGO_DB_URL)

            try:
                collection = mongo_client[database_name][collection_name]

                df = pd.DataFrame(list(collection.find()))

            finally:
                mongo_client.close()

            if "_id" in df.columns:
                df = df.drop(columns=["_id"])

            df.replace({"na": np.nan}, inplace=True)

            return df

        except Exception as e:
            raise NetworkSecurityException(e, sys) from e

    def export_data_into_feature_store(self, dataframe: pd.DataFrame):
        try:
            feature_store_file_path = (
                self.data_ingestion_config.feature_store_file_path
            )

            os.makedirs(
                os.path.dirname(feature_store_file_path),
                exist_ok=True
            )

            dataframe.to_csv(feature_store_file_path, index=False)

            logging.info("Feature store export completed")

            return dataframe

        except Exception as e:
            raise NetworkSecurityException(e, sys) from e

    def split_data_as_train_test(self, dataframe: pd.DataFrame):
        try:
            train_set, test_set = train_test_split(
                dataframe,
                test_size=self.data_ingestion_config.train_test_split_ratio,
                random_state=42
            )

            training_file_path = (
                self.data_ingestion_config.training_file_path
            )

            testing_file_path = (
                self.data_ingestion_config.testing_file_path
            )

            os.makedirs(os.path.dirname(training_file_path), exist_ok=True)
            os.makedirs(os.path.dirname(testing_file_path), exist_ok=True)

            train_set.to_csv(training_file_path, index=False)
            test_set.to_csv(testing_file_path, index=False)

            logging.info("Train and test datasets created successfully")

        except Exception as e:
            raise NetworkSecurityException(e, sys) from e

    def initiate_data_ingestion(self):
        try:
            logging.info("Data ingestion started")

            dataframe = self.export_collection_as_dataframe()

            dataframe = self.export_data_into_feature_store(dataframe)

            self.split_data_as_train_test(dataframe)

            dataingestionartifact = DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.testing_file_path
            )

            return dataingestionartifact

        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
