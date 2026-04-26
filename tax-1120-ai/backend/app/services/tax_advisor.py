def generate_advice(df):

    advice = []

    for _, row in df.iterrows():

        # Low confidence
        if row.get("confidence", 1) < 0.6:
            advice.append({
                "account": row["account_name"],
                "advice": "Low confidence classification. Needs manual review.",
                "impact": 0
            })

        # Meals rule (50% deductible)
        elif "meal" in row["account_name"].lower():
            advice.append({
                "account": row["account_name"],
                "advice": "Meals are only 50% deductible (IRS rule).",
                "impact": float(row["amount"]) * 0.5
            })

        # Penalty rule (not deductible)
        elif "penalty" in row["account_name"].lower():
            advice.append({
                "account": row["account_name"],
                "advice": "Penalties are NOT deductible.",
                "impact": float(row["amount"])
            })

    return advice