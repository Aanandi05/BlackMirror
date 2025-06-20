import requests

def is_valid_profile(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return False
        text = response.text.lower()
        # Check for common "not found" patterns across sites
        invalid_keywords = [
            "page not found",
            "this page isn’t available",
            "sorry, this page isn't available.",
            "not found",
            "doesn't exist",
            "user not found"
        ]
        return not any(keyword in text for keyword in invalid_keywords)
    except:
        return False

def guess_social_handles(email):
    email_prefix = email.split("@")[0]
    platforms = {
        "Instagram": f"https://instagram.com/{email_prefix}",
        "Reddit": f"https://www.reddit.com/user/{email_prefix}",
        "GitHub": f"https://github.com/{email_prefix}",
        "Twitter (X)": f"https://x.com/{email_prefix}"
    }

    found = []
    for platform, url in platforms.items():
        if is_valid_profile(url):
            found.append((platform, url))

    return found
