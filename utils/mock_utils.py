import random

def mock_google_dork_links(email):
    domain = email.split("@")[-1].split(".")[0]
    return [
        f"https://github.com/mockuser/{domain}-breach",
        f"https://pastebin.com/fakeLeak_{random.randint(1000,9999)}"
    ]

def mock_social_handles(email):
    handle = email.split("@")[0]
    return [
        ("Instagram", f"https://instagram.com/{handle}"),
        ("Reddit", f"https://reddit.com/user/{handle}"),
        ("GitHub", f"https://github.com/{handle}"),
    ]

def mock_pastebin_leaks(email):
    return [
        ("https://pastebin.com/fake1234", f"{email}: hashedpass123\nIP: 123.45.67.89"),
        ("https://pastebin.com/fake5678", f"{email} was found in an internal doc leak. Possible password: lovebug2020")
    ]

def mock_persona(email):
    return {
        "name": "Ashley Madison",
        "location": "New York, USA",
        "interests": ["Fashion", "Tech", "Music"],
        "job": "Product Manager at MockCorp",
        "linkedin": f"https://linkedin.com/in/{email.split('@')[0]}"
    }

def mock_phishing_email(persona):
    return f"""Subject: Urgent Account Verification Required

Hi {persona['name']},

We've noticed unusual activity on your account from {persona['location']}.  
Please verify your credentials immediately to avoid suspension.

Click below to confirm your details:
https://mock-secure-verify.com/{persona['name'].replace(" ", "").lower()}

Stay safe,
Security Team @ MockCorp
"""
