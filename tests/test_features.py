import pandas as pd
from src.features import add_derived_features, build_feature_pipeline, fit_transformers

def test_add_derived_features():
    df = pd.DataFrame({"HOUR":[0,12], "MONTH":[1,7]})
    out = add_derived_features(df)
    assert {"hour_sin","hour_cos","month_sin","month_cos"}.issubset(out.columns)

def test_pipeline_fit_transform():
    df = pd.DataFrame({
        "YEAR":[2017,2017,2016],
        "MONTH":[1,6,12],
        "DAY":[1,2,3],
        "HOUR":[0,12,23],
        "NEIGHBOURHOOD":["A","B","A"],
        "Latitude":[49.28, 49.26, 49.25],
        "Longitude":[-123.12, -123.1, -123.08],
        "TYPE":["Theft","Break and Enter","Theft"]
    })
    X = df.drop(columns=["TYPE"])
    preproc = build_feature_pipeline({}, X)
    X_tr = fit_transformers(preproc, X)
    assert X_tr.shape[0] == len(df)
