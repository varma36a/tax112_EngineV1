import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
import joblib

data = pd.DataFrame({
    "account_name": [
        "Sales Revenue", "Consulting Income",
        "Office Rent", "Employee Salary",
        "Client Meals", "Penalty Expense"
    ],
    "category": [
        "revenue", "revenue",
        "expense", "expense",
        "disallowed", "disallowed"
    ]
})

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data["account_name"])

encoder = LabelEncoder()
y = encoder.fit_transform(data["category"])

model = XGBClassifier()
model.fit(X, y)

joblib.dump(model, "app/ml/xgb_model.pkl")
joblib.dump(vectorizer, "app/ml/vectorizer.pkl")
joblib.dump(encoder, "app/ml/label_encoder.pkl")

print("Model trained ✅")