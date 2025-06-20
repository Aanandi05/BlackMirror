# main.py

from osint.google_dork import google_dork_search
from osint.social_guess import guess_social_handles
from osint.leak_scraper import check_pastebin_leaks
from osint.persona_builder import build_fake_persona
from osint.phishing_generator import generate_phishing_email
from report_generator import save_report

def banner():
    print("\n🕷️ Welcome to BlackMirror v2 — OSINT for the people\n")

def main():
    banner()
    email = input("📧 Enter target email: ").strip()

    print("\n🔎 Searching for public traces...\n")

    # 1. Google Dork Search
    print("🌐 Google Dork Results:")
    dork_links = google_dork_search(email)
    if not dork_links:
        print("  ❌ No public links found via dorking.")
    else:
        for i, link in enumerate(dork_links, 1):
            print(f"  [{i}] {link}")

    # 2. Social Handle Guessing
    print("\n👤 Social Handle Guessing:")
    handles = guess_social_handles(email)
    if not handles:
        print("  ❌ No social handles matched.")
    else:
        for platform, url in handles:
            print(f"  ✅ {platform}: {url}")

    # 3. Pastebin Leak Check
    print("\n🕳️ Pastebin Leak Check:")
    leaks = check_pastebin_leaks(email)
    if leaks:
        for link, snippet in leaks:
            print(f"  🔗 Found Leak: {link}")
            print(f"     📄 Snippet: {snippet[:100]}...\n")
    else:
        print("  ✅ No leaks found on Pastebin.")

    # 4. Fake Persona Creation
    persona = build_fake_persona(email)
    # 🧠 Build Fake Persona
    print("\n🧠 Inferred Persona:")
    print(f"  Name      : {persona['name']}")
    print(f"  Location  : {persona['location']}")
    print(f"  Job Title : {persona['job_title']}")
    print(f"  Company   : {persona['company']}")
    print(f"  Interests : {', '.join(persona['interests'])}")

    # 5. Generate Simulated Phishing Email
    print("\n📧 Simulated Phishing Email")
    print("--------------------------------------------")
    phishing_email = generate_phishing_email(persona, leaks)
    print(phishing_email)
    print("--------------------------------------------\n")



    save_report(
        email=email,
        dork_links=dork_links,
        social_profiles=handles,
        persona=persona,
        leaks=leaks,
        phishing_mail=phishing_email
    )
    print("\n📄 PDF report saved as BlackMirror_Report.pdf")


if __name__ == "__main__":
    main()
