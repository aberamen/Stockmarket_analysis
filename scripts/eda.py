from src.eda import load_data, analyze_headlines, sentiment_analysis, visualize_headlines

def main():
    filepath = "data/raw_analysis_rating.csv"
    df = load_data(filepath)
    df = analyze_headlines(df)
    df = sentiment_analysis(df)
    visualize_headlines(df)

if __name__ == "__main__":
    main()
