import matplotlib.pyplot as plt
import seaborn as sns

def plot_sentiment_vs_returns(analysis_df):
    """Plots sentiment scores against daily returns."""
    sns.scatterplot(x='avg_sentiment_score', y='daily_return', data=analysis_df)
    plt.title("Sentiment Score vs. Daily Stock Returns")
    plt.xlabel("Average Sentiment Score")
    plt.ylabel("Daily Stock Return (%)")
    plt.grid()
    plt.show()
