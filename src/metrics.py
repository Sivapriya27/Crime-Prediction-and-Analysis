from typing import Dict
import numpy as np
from sklearn.metrics import accuracy_score, f1_score, classification_report

def evaluate_predictions(y_true, y_pred, average="macro") -> Dict:
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "f1_macro": float(f1_score(y_true, y_pred, average=average)),
    }

def classification_report_dict(y_true, y_pred, average="macro") -> Dict:
    report = classification_report(y_true, y_pred, output_dict=True, zero_division=0)
    report["summary"] = {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "f1_macro": float(f1_score(y_true, y_pred, average=average)),
    }
    return report
