import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path

SSCHEMA_FILE_PATH = str(
    Path(__file__).resolve().parents[3]
    / "data_schema"
    / "schema.yaml"
)

TARGET_COLUMN = "CLASS_LABEL"

PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "phishingdata.csv"


SCHEMA_FILE_NAME=os.path.join("data_schema","schema.yaml")


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME

"""

DATA_INGESTION_COLLECTION_NAME: str="NetworkData"
DATA_INGESTION_DATABASE_NAME: str="BENSB"
DATA_INGESTION_DIR_NAME: str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str="feature_store"
DATA_INGESTION_INGESTION_DIR: str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float=0.2

"""
Data Validation related constant start with DATA_VALIDATION VAR NAME
"""

DATA_VALIDATION_DIR_NAME: str="data_validation"
DATA_VALIDATION_VALID_DIR: str="validated"
DATA_VALIDATION_INVALID_DIR: str="invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str="drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str="report.yaml"   



"""
Data Transformation related constants
"""

DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"

DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"

DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

PREPROCESSING_OBJECT_FILE_NAME: str = "preprocessing.pkl"


# KNN Imputer parameters
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform",
}
