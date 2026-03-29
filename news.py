import requests

# ----------- MOCK DATA (fallback) -----------

MOCK_NEWS = [
    {
        "title": "Nifty hits new high amid strong IT stocks",
        "description": "Indian stock markets reached new highs driven by IT sector growth and strong earnings."
    },
    {
        "title": "Startup funding rebounds in 2026",
        "description": "Venture capital investments increase as global markets stabilize."
    },
    {
        "title": "RBI signals stable interest rates",
        "description": "Reserve Bank of India hints at maintaining current rates due to controlled inflation."
    },
    {
        "title": "AI adoption rises in Indian enterprises",
        "description": "Companies increasingly invest in AI to improve operations and reduce costs."
    }
]


# ----------- REAL NEWS FETCH (OPTIONAL) -----------

def fetch_from_api(interests):
    """
    Try fetching real news (can fail if API not set)
    """
    try:
        API_KEY = "YOUR_NEWSAPI_KEY"  # replace if you have one

        query = " OR ".join(interests)

        url = f"https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}"

        response = requests.get(url)
        data = response.json()

        articles = []

        for item in data.get("articles", [])[:5]:
            articles.append({
                "title": item["title"],
                "description": item["description"] or ""
            })

        if len(articles) == 0:
            return MOCK_NEWS

        return articles

    except Exception:
        return MOCK_NEWS


# ----------- MAIN FUNCTION -----------

def fetch_news(interests):
    """
    Main function used by backend
    """
    # If you want ONLY safe demo → return MOCK_NEWS

    # return MOCK_NEWS   ← uncomment this for guaranteed demo

    # Otherwise try API
    return fetch_from_api(interests)