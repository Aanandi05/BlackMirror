import os
import requests
from dotenv import load_dotenv
from config import SERPAPI_API_KEY, USE_SERPAPI

USE_SERPAPI = os.getenv("USE_SERPAPI", "False").lower() == "true"

def google_dork_search(email):
    if not USE_SERPAPI:
        print("🔌 Skipping SerpAPI (disabled in .env)")
        return []

    query = f'intext:"{email}" site:github.com OR site:pastebin.com'
    url = "https://serpapi.com/search"
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_API_KEY
    }

    try:
        response = requests.get(url, params=params)
        results = response.json().get("organic_results", [])
        links = [r.get("link") for r in results if "link" in r]
        return links
    except Exception as e:
        print(f"❌ SerpAPI error: {e}")
        return []
