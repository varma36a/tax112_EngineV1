def compare_years(py_df, cy_df):

    # Revenue (credits → negative amounts)
    py_revenue = py_df[py_df["amount"] < 0]["amount"].sum()
    cy_revenue = cy_df[cy_df["amount"] < 0]["amount"].sum()

    # Deductions (debits → positive amounts)
    py_ded = py_df[py_df["amount"] > 0]["amount"].sum()
    cy_ded = cy_df[cy_df["amount"] > 0]["amount"].sum()

    return {
        "revenue_change": float(cy_revenue - py_revenue),
        "deduction_change": float(cy_ded - py_ded),
        "py_revenue": float(py_revenue),
        "cy_revenue": float(cy_revenue),
        "py_deductions": float(py_ded),
        "cy_deductions": float(cy_ded)
    }