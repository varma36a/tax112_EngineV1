import joblib
import numpy as np
from app.services.irs_mapping import IRS_MAP

model = joblib.load("app/ml/xgb_model.pkl")
vectorizer = joblib.load("app/ml/vectorizer.pkl")
encoder = joblib.load("app/ml/label_encoder.pkl")

def classify_accounts(df):

    X = vectorizer.transform(df["account_name"].astype(str))

    probs = model.predict_proba(X)
    preds = model.predict(X)

    df["category"] = encoder.inverse_transform(preds)
    df["confidence"] = probs.max(axis=1)

    df.loc[df["confidence"] < 0.6, "category"] = "review_needed"

    # IRS mapping
    df["irs_section"] = df["category"].map(IRS_MAP)

    return df