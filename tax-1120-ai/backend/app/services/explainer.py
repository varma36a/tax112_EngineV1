def generate_explanation(account_name, category):

    text = account_name.lower()

    rules = [
        ("penalty", "Contains keyword 'penalty' → IRS non-deductible expense"),
        ("meal", "Contains 'meal/food' → 50% deductible under IRS rules"),
        ("rent", "Rent-related → operating expense"),
        ("salary", "Employee compensation → deductible expense"),
        ("interest", "Interest → may be deductible depending on business use"),
        ("revenue", "Revenue keyword → classified as income"),
        ("sale", "Sales keyword → classified as income"),
    ]

    for keyword, reason in rules:
        if keyword in text:
            return reason

    return f"Model prediction based on learned patterns (confidence-driven)"