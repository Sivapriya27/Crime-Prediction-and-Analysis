# scripts/train.py
import os
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from src.features import build_feature_pipeline

# Paths
ARTIFACTS_DIR = "models/artifacts"
MODEL_PATH = "models/model.pkl"
os.makedirs(ARTIFACTS_DIR, exist_ok=True)

# Load training data
train_df = pd.read_csv("data/processed/train.csv")
X_train = train_df.drop('TYPE', axis=1)
y_train = train_df['TYPE']

# Build pipeline
pipeline = build_feature_pipeline()

# Fit features
X_train_transformed = pipeline.fit_transform(X_train)

# Fit model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_transformed, y_train)

# Save model & pipeline
joblib.dump(model, MODEL_PATH)
joblib.dump(pipeline, os.path.join(ARTIFACTS_DIR, "pipeline.joblib"))

print(f"Saved model to {MODEL_PATH}")
print(f"Saved pipeline to {ARTIFACTS_DIR}/pipeline.joblib")
