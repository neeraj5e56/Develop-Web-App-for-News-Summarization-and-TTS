import requests
from bs4 import BeautifulSoup

def scrape_news(company_name):
    # Replace spaces with "+" for the search query
    query = company_name.replace(" ", "+")
    url = f"https://news.google.com/search?q={query}"
    
    # Fetch the webpage
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract news articles
    articles = []
    for item in soup.find_all("article")[:10]:  # Limit to 10 articles
        # Find the title element with the new class name
        title_element = item.find("a", class_="WwrzSb")
        
        # Check if the title element exists
        if title_element:
            title = title_element.text
            link = "https://news.google.com" + title_element["href"].lstrip(".")
            articles.append({"title": title, "link": link})
        else:
            print("Warning: Could not find title element in article.")

    return articles

# Test the scraper
if __name__ == "__main__":
    company = input("Enter company name: ")
    news = scrape_news(company)
    for article in news:
        print(article)