"""
Cleans raw data and creates train/test CSVs for modeling.
"""
import pandas as pd
import numpy as np
from scripts.utils import get_logger, load_config, ensure_dirs
from src.data import load_raw, basic_clean, train_test_split_df

logger = get_logger("make_dataset")

def main():
    cfg = load_config()
    paths = cfg["paths"]
    data_cfg = cfg["data"]

    logger.info("Loading raw data...")
    df = load_raw(paths["raw"])

    logger.info("Basic cleaning...")
    df = basic_clean(df, data_cfg)

    logger.info("Train/test split...")
    train_df, test_df = train_test_split_df(df, test_size=data_cfg["test_size"], random_state=data_cfg["random_state"])

    ensure_dirs(paths["processed_train"])
    train_df.to_csv(paths["processed_train"], index=False)
    test_df.to_csv(paths["processed_test"], index=False)
    logger.info(f"Wrote {len(train_df)} train rows and {len(test_df)} test rows.")

if __name__ == "__main__":
    main()
