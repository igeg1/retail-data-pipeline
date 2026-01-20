import pandas
import src

def main():
    # File paths for raw data
    main_data = "data/raw/grocery_sales.csv"
    extra_data = "data/raw/extra_data.parquet"

    print("Starting ETL Process...")

    # Extract the raw data
    raw_data = src.extract(main_data, extra_data)

    # Transform (clean) the raw data
    clean_data = src.transform(raw_data)

    # Perform operations with the clean data
    agg_data = src.avg_weekly_sales_per_month(clean_data)

    # Preview data before saving
    print("\n-----Preview of clean data-----")
    print(clean_data.head(15))
    print("\n-----Preview of aggregated data-----")
    print(agg_data.head(12))

    # File paths to save transformed data
    clean_data_path = "data/processed/clean_data.csv"
    agg_data_path = "data/processed/agg_data.csv"

    # Load the transformed data to new CSV files
    src.load(clean_data, clean_data_path, agg_data, agg_data_path)
    print("\nETL Process Completed.")

if __name__ == "__main__":
    main()