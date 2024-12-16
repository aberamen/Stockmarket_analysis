import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob

def load_data(filepath):
    return pd.read_csv(filepath)

def analyze_headlines(df):
    df['headline_length'] = df['headline'].str.len()
    print(df['headline_length'].describe())
    return df

def sentiment_analysis(df):
    df['sentiment'] = df['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    print(df['sentiment'].describe())
    return df

def visualize_headlines(df):
    sns.histplot(df['headline_length'], bins=30, kde=True)
    plt.title("Headline Length Distribution")
    plt.show()

if __name__ == "__main__":
    data = load_data("data/raw_analysis_rating.csv")
    data = analyze_headlines(data)
    data = sentiment_analysis(data)
    visualize_headlines(data)
