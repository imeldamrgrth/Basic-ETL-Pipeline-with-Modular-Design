import pandas as pd

def clean_data(data):
    df = pd.DataFrame(data)

    df = df.drop_duplicates()
    df = df.dropna(subset=["Title", "Price", "Rating", "Colors"])
    df = df[df["Title"].str.lower() != "unknown product"]

    df = df[~df["Price"].str.contains("Price Unavailable", na=False)]
    df["Price"] = df["Price"].str.replace("$", "", regex=False)
    df["Price"] = pd.to_numeric(df["Price"], errors="coerce") * 16000
    df = df.dropna(subset=["Price"])
    df["Price"] = df["Price"].astype(float)

    df["Rating"] = df["Rating"].str.extract(r"(\d+\.\d+)").astype(float)
    df = df.dropna(subset=["Rating"])

    df["Colors"] = df["Colors"].str.extract(r"(\d+)").astype(float)
    df = df.dropna(subset=["Colors"])
    df["Colors"] = df["Colors"].astype(int)

    df["Size"] = df["Size"].astype(str).str.strip()
    df["Gender"] = df["Gender"].astype(str).str.strip()

    df.reset_index(drop=True, inplace=True)

    return df
