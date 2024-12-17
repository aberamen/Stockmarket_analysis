import matplotlib.pyplot as plt

def plot_stock_with_indicators(ticker, df, save_path):
    """Plot stock prices and indicators, and save the plot."""
    plt.figure(figsize=(14, 7))
    plt.plot(df['Close'], label=f'{ticker} Close Price', alpha=0.6)
    plt.plot(df['SMA_50'], label='50-day SMA', alpha=0.8)
    plt.plot(df['SMA_200'], label='200-day SMA', alpha=0.8)
    plt.title(f"{ticker} Stock Prices and Indicators")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid()
    plt.savefig(f"{save_path}/{ticker}_chart.png")
    plt.close()
