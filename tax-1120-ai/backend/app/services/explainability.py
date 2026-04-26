import json
import joblib
import numpy as np

from sklearn.metrics import confusion_matrix


def get_model_explainability():

    # Load metrics
    with open("app/ml/model_metrics.json") as f:
        metrics = json.load(f)

    # Load model + vectorizer
    model = joblib.load("app/ml/xgb_model.pkl")
    vectorizer = joblib.load("app/ml/vectorizer.pkl")
    encoder = joblib.load("app/ml/label_encoder.pkl")

    feature_names = vectorizer.get_feature_names_out()

    # 🔥 Feature Importance (Top 15)
    importance = model.feature_importances_
    indices = np.argsort(importance)[-15:]

    top_features = [
        {
            "feature": feature_names[i],
            "importance": float(importance[i])
        }
        for i in indices[::-1]
    ]

    # Clean metrics (remove accuracy/macro/weighted for table)
    class_metrics = {
        k: v for k, v in metrics.items()
        if k not in ["accuracy", "macro avg", "weighted avg"]
    }

    return {
        "accuracy": metrics.get("accuracy", 0),
        "macro_avg": metrics.get("macro avg", {}),
        "weighted_avg": metrics.get("weighted avg", {}),
        "class_metrics": class_metrics,
        "top_features": top_features
    }