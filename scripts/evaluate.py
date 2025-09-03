# scripts/evaluate.py
import pandas as pd
import joblib

# Paths
MODEL_PATH = "models/model.pkl"
PIPELINE_PATH = "models/artifacts/pipeline.joblib"
TEST_CSV = "data/processed/test.csv"
OUTPUT_CSV = "data/test_predictions.csv"

# Load model & pipeline
model = joblib.load(MODEL_PATH)
pipeline = joblib.load(PIPELINE_PATH)

# Load test data
test_df = pd.read_csv(TEST_CSV)
X_test = test_df.drop('TYPE', axis=1, errors='ignore')  # TYPE may not exist

# Transform & predict
X_test_transformed = pipeline.transform(X_test)
y_pred = model.predict(X_test_transformed)

# Add predictions to DataFrame
results = test_df.copy()
results['PREDICTED_TYPE'] = y_pred

# Save predictions
results.to_csv(OUTPUT_CSV, index=False)
print(f"Predictions saved to {OUTPUT_CSV}")

# Print summary counts
summary = results['PREDICTED_TYPE'].value_counts()
print("\nPrediction summary (counts of each crime type):")
print(summary)
