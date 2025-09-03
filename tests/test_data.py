import pandas as pd
from src.data import basic_clean

def test_basic_clean_keeps_target_and_time_fields():
    df = pd.DataFrame({
        "TYPE":["A","B"], "YEAR":[2017,2017], "MONTH":[1,2], "DAY":[1,2],
        "HOUR":[0,12], "NEIGHBOURHOOD":["X", None], "Latitude":[49.25,49.26],
        "Longitude":[-123.1,-123.0]
    })
    cfg = {"target":"TYPE", "random_state":42, "sample_frac":1.0}
    out = basic_clean(df, cfg)
    assert set(["TYPE","YEAR","MONTH","DAY","HOUR","NEIGHBOURHOOD","Latitude","Longitude"]).issubset(out.columns)
    assert out["NEIGHBOURHOOD"].isna().sum() == 0
