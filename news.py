import feedparser

def get_top_news():
    url = "https://feeds.bbci.co.uk/news/rss.xml"

    feed = feedparser.parse(url)

    headlines = []

    for entry in feed.entries[:10]:
        headlines.append(entry.title)

    return headlines


if __name__ == "__main__":
    headlines = get_top_news()

    print("\nTop Headlines\n")

    for i, headline in enumerate(headlines, 1):
        print(f"{i}. {headline}")