import pandas as pd
import numpy as np

def load_raw(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    # Standardize column names just in case
    df.columns = [c.strip().replace(" ", "_") for c in df.columns]
    # Map back common names
    rename_map = {
        "HUNDRED_BLOCK": "HUNDRED_BLOCK",
        "NEIGHBOURHOOD": "NEIGHBOURHOOD",
        "Latitude": "Latitude",
        "Longitude": "Longitude",
        "TYPE": "TYPE",
        "YEAR": "YEAR",
        "MONTH": "MONTH",
        "DAY": "DAY",
        "HOUR": "HOUR",
    }
    df = df.rename(columns=rename_map)
    return df

def basic_clean(df: pd.DataFrame, cfg: dict) -> pd.DataFrame:
    # Keep relevant columns if present
    keep = [cfg["target"], "YEAR", "MONTH", "DAY", "HOUR", "NEIGHBOURHOOD", "Latitude", "Longitude"]
    keep = [c for c in keep if c in df.columns]
    df = df[keep].copy()

    # Drop obviously bad rows
    df = df.dropna(subset=[cfg["target"]])

    # Fill missing times with zeros if absent
    for col in ["YEAR", "MONTH", "DAY", "HOUR"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)

    # Neighborhood: fill NA as "Unknown"
    if "NEIGHBOURHOOD" in df.columns:
        df["NEIGHBOURHOOD"] = df["NEIGHBOURHOOD"].fillna("Unknown").astype(str)

    # Lat/Long sanity (optional)
    for col in ["Latitude", "Longitude"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Optional down-sample for speed
    frac = cfg.get("sample_frac", 1.0)
    if 0 < frac < 1.0:
        df = df.sample(frac=frac, random_state=cfg["random_state"])

    df = df.reset_index(drop=True)
    return df

def train_test_split_df(df: pd.DataFrame, test_size: float=0.2, random_state: int=42):
    from sklearn.model_selection import train_test_split
    return train_test_split(df, test_size=test_size, random_state=random_state, stratify=df["TYPE"])
