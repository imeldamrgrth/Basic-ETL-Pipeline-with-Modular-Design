def save_to_csv(df, file_path="products.csv"):
    try:
        df.to_csv(file_path, index=False)
    except Exception as e:
        print(f"Gagal simpan CSV: {e}")
