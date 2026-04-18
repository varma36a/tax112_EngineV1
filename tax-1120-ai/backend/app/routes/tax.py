from fastapi import APIRouter, UploadFile
from app.services.tb_parser import parse_tb
from app.services.classifier import classify_accounts
from app.services.tax_engine import apply_tax_rules
from app.services.form1120 import generate_1120

router = APIRouter()

@router.post("/upload-tb")
async def upload_tb(file: UploadFile):

    df = parse_tb(file.file)
    df = classify_accounts(df)
    df = apply_tax_rules(df)

    result, breakdown = generate_1120(df)

    return {
        "result": result,
        "category_breakdown": breakdown,
        "preview": df.head(20).to_dict(orient="records")
    }