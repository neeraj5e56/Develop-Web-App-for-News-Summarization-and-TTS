from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Test sentiment analysis
if __name__ == "__main__":
    text = input("Enter text: ")
    sentiment = analyze_sentiment(text)
    print(f"Sentiment: {sentiment}")