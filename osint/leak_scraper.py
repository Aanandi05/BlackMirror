import os
import requests
from dotenv import load_dotenv

from config import SERPAPI_API_KEY, USE_SERPAPI


# Common headers to avoid being blocked
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def search_pastebin_links(email):
    if not USE_SERPAPI:
        print("🔌 Skipping Pastebin search (SerpAPI disabled)")
        return []
    query = f'intext:"{email}" site:pastebin.com'
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_API_KEY
    }

    try:
        response = requests.get("https://serpapi.com/search", params=params, headers=HEADERS)
        results = response.json().get("organic_results", [])
        links = [r.get("link") for r in results if "pastebin.com" in r.get("link", "")]
        return links
    except Exception as e:
        print(f"❌ Error fetching pastebin links: {e}")
        return []

def fetch_paste_content(url):
    try:
        print(f"🔍 Fetching: {url}")  # Add this for debug

        response = requests.get(url, headers=HEADERS, timeout=5)
        print(f"🔁 Status code: {response.status_code}")
        print(f"🔍 Snippet:\n{response.text[:200]}...\n")  # Optional: show sample HTML

        if response.status_code == 200 and "Pastebin.com" in response.text:
            return response.text
        else:
            return None
    except Exception as e:
        print(f"❌ Failed to fetch paste content: {e}")
        return None


def check_pastebin_leaks(email):
    print("🧾 Checking Pastebin for leaked data...")
    links = search_pastebin_links(email)
    if not links:
        print("❌ No Pastebin results found.")
        return []

    leaked_data = []
    for link in links:
        content = fetch_paste_content(link)
        if content and email in content:
            leaked_data.append((link, content[:300]))  # show first 300 chars
    return leaked_data
