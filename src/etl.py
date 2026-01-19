import pandas as pd

def extract(store_data, extra_data, column = "index"):
    """
    Extracts data from a .csv source and a .parquet source and merges the data on the specified column.
    
    :param store_data: File path to a CSV file.
    :param extra_data: File path to a .parquet file.
    :param column: Label (name) of the column to merge the two DataFrames on.
    :return: A pandas DataFrame with the raw, merged data.
    """

    store_data_df = pd.read_csv(store_data)
    extra_df = pd.read_parquet(extra_data, engine="fastparquet")
    merged_df = store_data_df.merge(extra_df, on = column)
    return merged_df

def load(full_data, full_data_file_path, agg_data, agg_data_file_path):
    """
    Loads two pandas DataFrames into two separate .csv files using the specified paths.
    
    :param full_data: Pandas DataFrame with the full, clean data.
    :param full_data_file_path: String with a file path to save full_data to.
    :param agg_data: Pandas DataFrame with the aggregated sales data.
    :param agg_data_file_path: String with a file path to save agg_datas to.
    """

    # Write the full data to a CSV
    full_data.to_csv(full_data_file_path, index=False)

    # Write the aggregated data to a CSV
    agg_data.to_csv(agg_data_file_path, index=False)