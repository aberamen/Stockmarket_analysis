import talib

def add_indicators(df):
    """Add technical indicators to the DataFrame."""
    df['SMA_50'] = talib.SMA(df['Close'], timeperiod=50)  # 50-day SMA
    df['SMA_200'] = talib.SMA(df['Close'], timeperiod=200)  # 200-day SMA
    df['RSI'] = talib.RSI(df['Close'], timeperiod=14)  # RSI
    df['MACD'], df['Signal'], df['Hist'] = talib.MACD(
        df['Close'], fastperiod=12, slowperiod=26, signalperiod=9
    )
    return df
