def aggregate_sentiments(news_df):
    """Aggregates daily sentiment scores."""
    daily_sentiment = news_df.groupby('date')['sentiment_score'].mean().reset_index()
    daily_sentiment.rename(columns={'sentiment_score': 'avg_sentiment_score'}, inplace=True)
    return daily_sentiment

def merge_and_calculate_correlation(stock_df, sentiment_df):
    """Merges datasets and calculates correlation."""
    analysis_df = pd.merge(stock_df[['date', 'daily_return']], sentiment_df, on='date', how='inner')
    correlation = analysis_df['daily_return'].corr(analysis_df['avg_sentiment_score'])
    return analysis_df, correlation
