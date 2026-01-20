import pandas as pd
import pytest
from src.business import transform
from src.business import avg_weekly_sales_per_month

@pytest.fixture(scope="module")
def raw_data():
    raw_data = pd.DataFrame({
        'Unnamed: 0': [0, 1, 2, 3, 4, 5, 6],
        'index': [0, 1, 2, 3, 4, 5, 6],
        'Store_ID': [1, 1, 1, 1, 1, 1, 1],
        'Date': ['2010-02-05', None, '2010-03-01', '2010-03-01', '2010-04-05', '2011-02-05', '2011-03-01'],
        'Dept': [1, 5, 10, 28, 13, 49, 72],
        'Weekly_Sales': [46729.77, 21249.31, 11737.12, None, 19047.05, 0, 10000.0],
        'IsHoliday': [0, 0, 0, 0, 0, 0, 0],
        'Temperature': [19.3, 19.3, 19.3, 25.0, 20.9, 28.7, 29.1],
        'Fuel-Price': [0, 0, 0, 0, 0, 0, 0],
        'MarkDown1': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        'CPI': [211.096358, 211.096358, 211.096358, 211.096358, 211.096358, None, 211.096358],
        'Unemployment': [8.106, None, 8.106, None, None, None, 8.106]
    })
    return raw_data

@pytest.fixture(scope="module")
def clean_data(raw_data):
    clean_data = transform(raw_data)
    return clean_data

@pytest.fixture(scope="module")
def agg_data(clean_data):
    agg_data = avg_weekly_sales_per_month(clean_data)
    return agg_data


def test_transform_columns(clean_data):
    expected_columns = ['Store_ID', 'Dept', 'IsHoliday', 'Weekly_Sales', 'CPI', 'Unemployment', 'Month']

    assert clean_data.columns.tolist() == expected_columns


def test_transform_imputes_missing_values(clean_data):
    # Assert there are no NaN values in any column
    assert clean_data['Weekly_Sales'].isnull().sum() == 0
    assert clean_data['CPI'].isnull().sum() == 0
    assert clean_data['Unemployment'].isnull().sum() == 0


def test_transform_ignores_smaller_sales(clean_data):
    valid_sales = [46729.77, 21249.31, 11737.12, 19047.05, 10000.0]

    # Assert that only records w/ sales above 10_000 were kept
    assert clean_data['Weekly_Sales'].sum() == sum(valid_sales)


def test_transform_extracts_month(clean_data):
    expected_months = [2, 2, 3, 4, 3] 

    # Assert Months were successfully extracted from Date
    assert clean_data['Month'].tolist() == expected_months


def test_avg_sales_grouping_sorting(agg_data):
    expected_values = [2, 3, 4]

    # Asert the results were properly grouped into Months and sorted in order
    assert agg_data['Month'].to_list() == expected_values


def test_avg_sales_rounding(agg_data):
    avg_sale_m2 = round((46729.77 + 21249.31) / 2, 2)
    avg_sale_m3 = round((11737.12 + 10000.0) / 2, 2)
    expected_values = [avg_sale_m2, avg_sale_m3, 19047.05] 

    # Assert the results match the expected values
    assert agg_data['Weekly_Sales'].to_list() == expected_values