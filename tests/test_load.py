import pandas as pd
from utils.load import save_to_csv

def test_save_to_csv(tmp_path):
    df = pd.DataFrame({
        'Title': ['Batik Casual'],
        'Price': [100000],
        'Rating': [4.5],
        'Colors': [2],
        'Size': ['L'],
        'Gender': ['Unisex']
    })

    file_path = tmp_path / "test_output.csv"
    save_to_csv(df, file_path)

    assert file_path.exists()

    df_loaded = pd.read_csv(file_path)
    pd.testing.assert_frame_equal(df.reset_index(drop=True), df_loaded)
