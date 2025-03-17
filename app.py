import streamlit as st
from scraper import scrape_news
from sentiment import analyze_sentiment
from tts import generate_tts

st.title("News Summarization and Sentiment Analysis")

# Input: Company name
company_name = st.text_input("Enter Company Name")

# Button: Analyze
if st.button("Analyze"):
    st.write(f"Fetching news for {company_name}...")
    
    # Scrape news articles
    articles = scrape_news(company_name)
    
    # Display articles and analyze sentiment
    for article in articles:
        st.write(f"**Title:** {article['title']}")
        sentiment = analyze_sentiment(article['title'])
        st.write(f"**Sentiment:** {sentiment}")
    
    # Generate Hindi TTS summary
    summary = f"News analysis for {company_name} is complete."
    generate_tts(summary)
    st.audio("output.mp3")