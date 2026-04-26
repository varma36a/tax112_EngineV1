import pandas as pd
import numpy as np
import joblib
import json
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

from xgboost import XGBClassifier


# =========================
# 📂 Load Data
# =========================
DATA_PATH = "app/data/training_data_large.csv"

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"❌ Training data not found at {DATA_PATH}")

df = pd.read_csv(DATA_PATH)

# Clean
df = df.dropna()
df["account_name"] = df["account_name"].astype(str).str.lower()

print(f"✅ Loaded {len(df)} rows")


# =========================
# 🔤 Feature Engineering
# =========================
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    max_features=500
)

X = vectorizer.fit_transform(df["account_name"])


# =========================
# 🏷️ Labels
# =========================
encoder = LabelEncoder()
y = encoder.fit_transform(df["category"])

print("📊 Classes:", list(encoder.classes_))


# =========================
# ✂️ Train/Test Split
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y   # ensures class balance
)


# =========================
# 🤖 Model
# =========================
model = XGBClassifier(
    n_estimators=200,
    max_depth=4,
    learning_rate=0.1,
    use_label_encoder=False,
    eval_metric='mlogloss'
)

model.fit(X_train, y_train)


# =========================
# 📊 Evaluation (FIXED)
# =========================
preds = model.predict(X_test)

accuracy = accuracy_score(y_test, preds)

print("\n📊 MODEL PERFORMANCE")
print("---------------------------")
print(f"Accuracy: {accuracy:.4f}")

# ✅ FIX: no target_names mismatch
print("\nClassification Report:\n")
print(classification_report(y_test, preds))


# =========================
# 💾 Save Model
# =========================
os.makedirs("app/ml", exist_ok=True)

joblib.dump(model, "app/ml/xgb_model.pkl")
joblib.dump(vectorizer, "app/ml/vectorizer.pkl")
joblib.dump(encoder, "app/ml/label_encoder.pkl")

print("\n✅ Model saved → app/ml/")


# =========================
# 📁 Save Metrics (for UI)
# =========================
metrics = classification_report(y_test, preds, output_dict=True)

with open("app/ml/model_metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)

print("📁 Metrics saved → app/ml/model_metrics.json")