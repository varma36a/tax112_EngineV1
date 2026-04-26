from fastapi import APIRouter, UploadFile
import numpy as np

from app.services.tb_parser import parse_tb
from app.services.classifier import classify_accounts
from app.services.tax_engine import apply_tax_rules
from app.services.form1120 import generate_1120
from app.services.advisor import generate_advice
from app.services.explainer import generate_explanation
from app.services.explainability import get_model_explainability


router = APIRouter()

@router.get("/explainability")
def explainability():
    return get_model_explainability()


@router.post("/upload-tb")
async def upload_tb(file: UploadFile):

    df = parse_tb(file.file)

    df = classify_accounts(df)
    df = apply_tax_rules(df)

    # 🔍 Add explanation
    df["explanation"] = df.apply(
        lambda x: generate_explanation(x["account_name"], x["category"]),
        axis=1
    )

    # 💡 Advisor
    advice = generate_advice(df)

    result = generate_1120(df)

    # safety fix
    df = df.replace([np.inf, -np.inf], 0)
    df = df.fillna(0)

    return {
        "result": result,
        "preview": df.to_dict(orient="records"),
        "advice": advice,
        "category_breakdown": df.groupby("category")["amount"].sum().to_dict()
    }