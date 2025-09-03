from typing import Dict
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb

def build_model(cfg: Dict):
    algo = cfg["model"]["algorithm"]
    if algo == "logistic":
        p = cfg["model"]["logistic"]
        return LogisticRegression(C=p["C"], max_iter=p["max_iter"], n_jobs=None)
    if algo == "random_forest":
        p = cfg["model"]["random_forest"]
        return RandomForestClassifier(
            n_estimators=p["n_estimators"],
            max_depth=p["max_depth"],
            n_jobs=p["n_jobs"],
            class_weight=p["class_weight"],
            random_state=42
        )
    if algo == "xgboost":
        p = cfg["model"]["xgboost"]
        return xgb.XGBClassifier(
            n_estimators=p["n_estimators"],
            learning_rate=p["learning_rate"],
            max_depth=p["max_depth"],
            subsample=p["subsample"],
            colsample_bytree=p["colsample_bytree"],
            eval_metric=p["eval_metric"],
            random_state=42,
            tree_method="hist"
        )
    raise ValueError(f"Unknown algorithm: {algo}")
