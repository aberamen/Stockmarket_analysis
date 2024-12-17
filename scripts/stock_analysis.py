def calculate_daily_returns(stock_df):
    """Calculates daily percentage changes in stock prices."""
    stock_df['daily_return'] = stock_df['Close'].pct_change() * 100
    return stock_df
