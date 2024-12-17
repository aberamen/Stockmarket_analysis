import pandas as pd

def load_stock_data(filepath):
    """Load stock price data from a CSV file."""
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'])  # Convert 'Date' column to datetime
    df.set_index('Date', inplace=True)      # Set 'Date' as the index
    return df
