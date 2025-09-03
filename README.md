# Crime Prediction & Analysis (Vancouver) - ML Pipeline

End-to-end, reproducible ML project that predicts **crime type** from time/location/context using the Vancouver Police open data (via Kaggle) by Supervised Machine Learning - Classification. 
Includes data download, cleaning/feature engineering, modeling, evaluation, error analysis, and tests.

---

## Features
- Clean and process raw crime data
- Cyclical feature engineering for time
- Categorical encoding and numeric scaling
- Train ML models (Random Forest, Logistic Regression, XGBoost)
- Predict and save crime types for new data
- EDA and error analysis notebooks

---

## Concepts Used

### 1. Supervised Machine Learning - Classification
- **Target Variable:** `TYPE` (crime type)  
- **Input Features:** Time, location, and other categorical features  
### 2. Feature Engineering
- **Cyclical Features:** Transformed time-based features using sine and cosine functions:  
  - `month_sin`, `month_cos`  
  - `hour_sin`, `hour_cos`  
- **Categorical Encoding:** One-hot encoding applied to `NEIGHBOURHOOD`  
- **Numeric Scaling:** StandardScaler applied to `latitude` and `longitude`  
### 3. Pipeline
- Utilizes **`ColumnTransformer` + `Pipeline`** to ensure consistent transformation of both training and test datasets  
### 4. Modeling
- **Primary Model:** Random Forest (default)  
- **Alternative Options:** Logistic Regression, XGBoost  
- Supports **multi-class classification**  
### 5. Evaluation
- Predictions are saved as CSV files  
- Summaries include counts of each predicted class  
- **Error Analysis:** Jupyter notebook available to inspect correct vs. incorrect predictions  
### 6. Testing
- Unit tests for feature engineering and data cleaning:  
  - `tests/test_features.py`  
  - `tests/test_data.py`

---

## Tools & Libraries
- Python 3, pandas, numpy, scikit-learn, xgboost, matplotlib, seaborn, joblib, pyyaml, kaggle API

---

## 📦 Project Structure

- data/ – Contains all datasets
- raw/ – Original/raw CSVs (e.g., downloaded from Kaggle)
- interim/ – Cleaned/intermediate data used during processing
- processed/ – Final train/test datasets used for modeling

- models/ – Stores trained models and pipeline artifacts
- model.pkl – Trained machine learning model

- artifacts/ – Feature pipelines and transformers (e.g., pipeline.joblib)

- notebooks/ – Jupyter notebooks for exploration and analysis
- 01_eda.ipynb – Exploratory Data Analysis (plots, counts, distributions)
- 02_error_analysis.ipynb – Evaluate predictions and inspect errors

- scripts/ – Python scripts for workflow automation
- download_data.py – Download dataset from Kaggle if not already present
- make_dataset.py – Clean raw data, create train/test CSVs
- train.py – Train model and save pipeline
- evaluate.py – Predict on test data, save results, summarize predictions
- utils.py – Logging, config loading, and utility functions

- src/ – Source code for modular functionality
- data.py – Data loading and cleaning functions (basic_clean, load_raw)
- features.py – Feature engineering, pipeline creation (add_derived_features, build_feature_pipeline)

- tests/ – Unit tests for code validation
- test_data.py – Tests for data cleaning functions
- test_features.py – Tests for feature engineering and pipelines

- .gitignore – Ignore compiled files, cache, models, and processed data
- config.yaml – Configuration file for paths, model parameters, feature settings
- requirements.txt – Python dependencies (pandas, numpy, scikit-learn, xgboost, matplotlib, seaborn, joblib, pyyaml, kaggle, tabulate)

---

## 🗂 Dataset

**Kaggle**: Crime in Vancouver (2003–2017). This dataset includes columns like TYPE, YEAR, MONTH, DAY, HOUR, MINUTE, HUNDRED_BLOCK, NEIGHBOURHOOD, X, Y, Latitude, Longitude. 

Kaggle API notes : Create ~/.kaggle/kaggle.json with your API token (from Kaggle → Account → Create New Token).

Or manually download the CSV from Kaggle and drop it into data/raw/ as crime.csv.
The downloader script will detect it and skip the API call.

---

## 8️⃣ Nice-to-Haves / Next Steps

- Add metrics like **accuracy**, **F1-score**, and **confusion matrix** in evaluation  
- Add **geospatial plots** using latitude/longitude (e.g., heatmaps, hexbin)  
- Support **XGBoost** and **hyperparameter tuning**  
- Add **interactive dashboard** for predictions or EDA  
- More sophisticated features: **day-of-week**, **holiday indicator**, **weather**, **population density**

---

## 🔧 Troubleshooting

No Kaggle credentials? Place crime.csv in data/raw/ and re-run.

Memory errors? Decrease train.sample_frac in config.yaml.

Plot issues on headless servers? Set MPLBACKEND=Agg.

---

## Quick Start
```bash
# Setup environment
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

# Download dataset
python -m scripts.download_data

# Prepare train/test datasets
python -m scripts.make_dataset

# Train model
python -m scripts.train

# Predict & evaluate
python -m scripts.evaluate

#Inspect EDA & Errors
Open notebooks: notebooks/01_eda.ipynb and notebooks/02_error_analysis.ipynb
