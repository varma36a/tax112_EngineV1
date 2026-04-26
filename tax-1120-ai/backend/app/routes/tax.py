from fastapi import APIRouter, UploadFile, File
import numpy as np

from app.services.tb_parser import parse_tb
from app.services.classifier import classify_accounts
from app.services.tax_engine import apply_tax_rules
from app.services.form1120 import generate_1120
from app.services.tax_advisor import generate_advice
from app.services.comparison import compare_years

router = APIRouter()


# 🔧 Clean dataframe
def clean_dataframe(df):
    df = df.replace([np.inf, -np.inf], 0)
    df = df.fillna(0)
    return df


# 🔧 Convert dict values to float
def to_float_dict(d):
    return {k: float(v) for k, v in d.items()}


# =========================
# 📤 Upload TB
# =========================
@router.post("/upload-tb")
async def upload_tb(file: UploadFile = File(...)):

    try:
        df = parse_tb(file.file)
        df = classify_accounts(df)
        df = apply_tax_rules(df)

        df = clean_dataframe(df)

        # ✅ FIX HERE (tuple unpacking)
        result, breakdown = generate_1120(df)

        result = to_float_dict(result)
        breakdown = to_float_dict(breakdown)

        advice = generate_advice(df)

        preview = df.head(20).to_dict(orient="records")

        return {
            "result": result,
            "category_breakdown": breakdown,
            "advice": advice,
            "preview": preview
        }

    except Exception as e:
        return {"error": str(e)}


# =========================
# 📊 Compare
# =========================
@router.post("/compare")
async def compare(py_file: UploadFile = File(...),
                  cy_file: UploadFile = File(...)):

    try:
        py_df = parse_tb(py_file.file)
        cy_df = parse_tb(cy_file.file)

        py_df = clean_dataframe(py_df)
        cy_df = clean_dataframe(cy_df)

        comparison = compare_years(py_df, cy_df)

        comparison = to_float_dict(comparison)

        return comparison

    except Exception as e:
        return {"error": str(e)}