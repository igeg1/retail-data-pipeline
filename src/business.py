import pandas as pd

def transform(raw_data):
    """
    Performs a series of transformations on the raw_data to prepare it for loading and analysis.

    Makes a copy of the raw_data with only specified columns. 
    Forward fills missing data. 
    Strips Month from Date and drops Date.
    Keeps only records with Weekly_Sales > $ 10_000
    
    :param raw_data: A pandas DataFrame with recently extracted, raw sales data.
    :return: A cleaned pandas DataFrame. 
    """

    # Making a copy of the raw_data with only the columns necessary
    cols_to_keep = ['Store_ID', 'Date', 'Dept', 'IsHoliday', 'Weekly_Sales', 'CPI', 'Unemployment']
    clean_data = raw_data[cols_to_keep].copy()

    # Filling in missing Date and CPI, and Unemployment data using last valid observations
    clean_data['Date'] = clean_data['Date'].ffill()
    clean_data['CPI'] = clean_data['CPI'].ffill()
    clean_data['Unemployment'] = clean_data['Unemployment'].ffill()

    # Strip Month from Date
    clean_data['Date'] = pd.to_datetime(clean_data['Date'])
    clean_data['Month'] = clean_data['Date'].dt.month
    clean_data = clean_data.drop(columns=['Date'])

    # Maintain records with Weekly_Sales > $10_000
    min_sales = 10000
    clean_data = clean_data[clean_data['Weekly_Sales'] >= min_sales]

    return clean_data


def avg_weekly_sales_per_month(clean_data):
    """
    Aggregates retail data to calculate the average weekly sales for each month.

    The function groups the data by the 'Month' column, computes the mean of 
    'Weekly_Sales', and ensures the final output is sorted chronologically 
    and formatted for financial reporting with two-decimal precision.
    
    :param clean_data: A pandas DataFrame with recently transformed, clean data.
    :return: A pandas DataFrame with only two columns: Month and Weekly_Sales.
    """

    # Make a copy of clean_data with relevant columns
    agg_data = clean_data[['Month', 'Weekly_Sales']].copy() 

    # Group by Month and calculate the mean / average Weekly_Sales
    agg_data = agg_data.groupby(['Month']).mean()

    # Round to two decimals
    agg_data = agg_data.round(2)

    # Sort by Month in increasing order
    agg_data = agg_data.sort_values(by='Month', ascending=True)
    
    # Reset the index 
    agg_data = agg_data.reset_index()
    
    return agg_data