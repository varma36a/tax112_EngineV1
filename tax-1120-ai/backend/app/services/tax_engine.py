def apply_tax_rules(df):

    # Example adjustments
    df.loc[df["account_name"].str.contains("meal", case=False), "amount"] *= 0.5
    df.loc[df["account_name"].str.contains("penalty", case=False), "amount"] = 0

    return df