def generate_advice(df):

    advice = []

    for _, row in df.iterrows():

        category = row["category"]
        amount = row["amount"]
        name = row["account_name"]
        confidence = row["confidence"]

        item = {
            "account": name,
            "category": category,
            "confidence": round(confidence, 2),
            "impact": 0,
            "advice": ""
        }

        # 🔴 Low confidence warning
        if confidence < 0.6:
            item["advice"] = "⚠️ Low confidence classification. Needs manual review."
            advice.append(item)
            continue

        # 🟡 Meals (50% deductible)
        if category == "meals":
            item["impact"] = amount * 0.5
            item["advice"] = "Only 50% of meals are deductible. Consider optimizing."

        # 🔴 Penalty (non-deductible)
        elif category == "penalty":
            item["impact"] = 0
            item["advice"] = "Penalty is non-deductible. Avoid for tax savings."

        # 🟢 Expense (good)
        elif category == "expense":
            item["impact"] = amount
            item["advice"] = "Fully deductible business expense."

        # 🟢 Income
        elif category == "income":
            item["impact"] = amount
            item["advice"] = "Revenue contributes to taxable income."

        # 🟡 Charity
        elif category == "charity":
            item["impact"] = amount * 0.6
            item["advice"] = "Charity may be partially deductible under limits."

        else:
            item["advice"] = "General classification applied."

        advice.append(item)

    return advice