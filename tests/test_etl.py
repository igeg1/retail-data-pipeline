import numpy as np
import os
import pandas as pd
import pytest
from src.etl import extract
from src.etl import load


@pytest.fixture()
def clean_data():
    return "data/processed/clean_data.csv"

@pytest.fixture()
def agg_data():
    return "data/processed/agg_data.csv"


def test_processed_files_exist(clean_data, agg_data):
    # Assert files exist in said paths
    assert os.path.exists(clean_data), "Clean data CSV was not created."
    assert os.path.exists(agg_data), "Monthly sales report was not created."


def test_processed_files_schemas(clean_data, agg_data):
    expected_clean_cols = ['Store_ID', 'Dept', 'IsHoliday', 'Weekly_Sales', 'CPI', 'Unemployment', 'Month']
    expected_agg_cols = ['Month', 'Weekly_Sales']

    # Read the files and validate columns
    clean_df = pd.read_csv(clean_data)
    agg_df = pd.read_csv(agg_data)

    # Assertions to check schemas match
    assert list(clean_df.columns) == expected_clean_cols, f"Schema mismatch in {clean_data}"
    assert list(agg_df.columns) == expected_agg_cols, f"Schema mismatch in {agg_data}"


def test_processed_data_types(agg_data):    
    df = pd.read_csv(agg_data)
    
    # Assertions for the Aggregated Report
    assert np.issubdtype(df['Month'].dtype, np.integer), f"Month should be integer, got {df['Month'].dtype}"
    assert np.issubdtype(df['Weekly_Sales'].dtype, np.floating), f"Sales should be float, got {df['Weekly_Sales'].dtype}"