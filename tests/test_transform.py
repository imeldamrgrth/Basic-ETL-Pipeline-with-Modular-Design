import pytest
import pandas as pd
from utils.transform import clean_data

def test_clean_data():
    sample_data = pd.DataFrame({
        "Title": ["T-Shirt", "Unknown Product", None],
        "Price": ["$10", "Price Unavailable", "$15"],
        "Rating": ["4.8 / 5", "Invalid Rating", "3.2 / 5"],        
        "Colors": ["3 Colors", None, "1 Color"],
        "Size": ["Size: M", "Size: L", "Size: XL"],
        "Gender": ["Gender: Male", "Gender: Female", None],        
        "timestamp": ["2024-05-12T00:00:00"]*3
    })

    df_cleaned = clean_data(sample_data)

    assert not df_cleaned.empty
    assert pd.api.types.is_float_dtype(df_cleaned["Price"])
    assert pd.api.types.is_integer_dtype(df_cleaned["Colors"])
    assert pd.api.types.is_float_dtype(df_cleaned["Rating"])
    assert all(df_cleaned["Title"].str.lower() != "unknown product")
    assert all(df_cleaned["Price"] > 0)
    assert all((df_cleaned["Rating"] >= 0) & (df_cleaned["Rating"] <= 5))
    assert all(df_cleaned["Colors"] > 0)
