import os
from src.data_loader import load_stock_data
from src.indicators import add_indicators
from src.visualizations import plot_stock_with_indicators

# File paths
DATA_DIR = "project/data/"
RESULT_DIR = "project/task-2/results/processed_data/"
CHART_DIR = "project/task-2/results/"

# Stock files
stock_files = {
    "AAPL": f"{DATA_DIR}/AAPL_historical_data.csv",
    "AMZN": f"{DATA_DIR}/AMZN_historical_data.csv",
    "GOOG": f"{DATA_DIR}/GOOG_historical_data.csv",
    "META": f"{DATA_DIR}/META_historical_data.csv",
    "MSFT": f"{DATA_DIR}/MSFT_historical_data.csv",
    "NVDA": f"{DATA_DIR}/NVDA_historical_data.csv",
    "TSLA": f"{DATA_DIR}/TSLA_historical_data.csv",
}

if not os.path.exists(RESULT_DIR):
    os.makedirs(RESULT_DIR)

if not os.path.exists(CHART_DIR):
    os.makedirs(CHART_DIR)

# Process each stock
for ticker, filepath in stock_files.items():
    print(f"Processing {ticker}...")
    # Load stock data
    df = load_stock_data(filepath)

    # Add indicators
    df = add_indicators(df)

    # Save processed data
    df.to_csv(f"{RESULT_DIR}/{ticker}_processed.csv")
    print(f"Saved processed data for {ticker} at {RESULT_DIR}/{ticker}_processed.csv")

    # Plot and save chart
    plot_stock_with_indicators(ticker, df, CHART_DIR)
    print(f"Saved chart for {ticker} at {CHART_DIR}/{ticker}_chart.png")

print("Task 2 completed!")
