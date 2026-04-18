def generate_1120(df):

    revenue = df[df["amount"] < 0]["amount"].sum() * -1
    deductions = df[df["amount"] > 0]["amount"].sum()

    taxable_income = revenue - deductions
    tax = taxable_income * 0.21

    breakdown = df.groupby("category")["amount"].sum().to_dict()

    return {
        "gross_receipts": float(revenue),
        "deductions": float(deductions),
        "taxable_income": float(taxable_income),
        "tax": float(tax)
    }, breakdown