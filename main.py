from utils.extract import scrape_main
from utils.transform import clean_data
from utils.load import save_to_csv
import time
from tabulate import tabulate

def run_etl():
    all_data = []
    for page in range(1, 51):
        print(f"Scraping page {page}")
        all_data.extend(scrape_main(page))
        time.sleep(1)

    print(f"Total raw data: {len(all_data)}")

    clean_df = clean_data(all_data)
    print(f"Total cleaned data: {len(clean_df)}")

    # Format Price ke string rapi tanpa scientific notation tapi tetap DataFrame
    def format_price(x):
        return f"{x:.0f}"

    df_print = clean_df.head(10).copy()
    df_print['Price'] = df_print['Price'].map(format_price)

    print(tabulate(df_print, headers='keys', tablefmt='psql'))

    save_to_csv(clean_df)

if __name__ == "__main__":
    run_etl()
