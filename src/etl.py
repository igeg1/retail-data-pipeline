import pandas as pd

def extract(store_data, extra_data, column = "index"):
    """
    Extracts data from a .csv source and a .parquet source and merges the data on the specified column.
    
    :param store_data: File path to a CSV file.
    :param extra_data: File path to a .parquet file.
    :param column: Label (name) of the column to merge the two DataFrames on.
    """
    store_data_df = pd.read_csv(store_data)
    extra_df = pd.read_parquet(extra_data, engine="fastparquet")
    merged_df = store_data_df.merge(extra_df, on = column)
    return merged_df
