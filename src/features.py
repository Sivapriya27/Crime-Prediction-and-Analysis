# src/features.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler, FunctionTransformer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def add_cyclical_features(X):
    X = X.copy()
    X['month_sin'] = np.sin(2 * np.pi * X['MONTH'] / 12)
    X['month_cos'] = np.cos(2 * np.pi * X['MONTH'] / 12)
    X['hour_sin'] = np.sin(2 * np.pi * X['HOUR'] / 24)
    X['hour_cos'] = np.cos(2 * np.pi * X['HOUR'] / 24)
    return X

def build_feature_pipeline():
    # Columns
    numeric_cols = ['Latitude', 'Longitude']
    cat_cols = ['NEIGHBOURHOOD']

    # Numeric pipeline
    num_transformer = Pipeline([
        ('scaler', StandardScaler())
    ])

    # Categorical pipeline
    cat_transformer = Pipeline([
        ('ohe', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])

    # Full column transformer
    preprocessor = ColumnTransformer([
        ('num', num_transformer, numeric_cols),
        ('cat', cat_transformer, cat_cols)
    ], remainder='passthrough')  # passthrough cyclical features

    # Full pipeline including cyclical feature function
    full_pipeline = Pipeline([
        ('cyclical', FunctionTransformer(add_cyclical_features)),
        ('preprocess', preprocessor)
    ])

    return full_pipeline
