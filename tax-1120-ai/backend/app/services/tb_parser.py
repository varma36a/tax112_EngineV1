import pandas as pd

def parse_tb(file):

    df = pd.read_excel(file)

    df.columns = [c.lower() for c in df.columns]

    df["amount"] = df["debit"].fillna(0) - df["credit"].fillna(0)

    return df