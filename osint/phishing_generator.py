## modules/phishing_generator.py
import random

TEMPLATES = [
    """
Hi {name},

Your login credentials were found in a public data breach ({leak}).
As a {job} at {company}, your digital security is crucial.

Take action now: https://urgent-reset.com
Stay safe,
CyberSec Team
    """,
    """
Dear {name},

Your account security is at risk. We’ve identified leaked data ({leak}) connected to your credentials.

Recommended Action: Reset your password ASAP.

Sincerely,
Internal IT Support
    """
]

def generate_phishing_email(persona, leaks):
    name = persona.get("name", "user")
    job = persona.get("job_title", "professional")
    company = persona.get("company", "TechCorp")
    leak = leaks[0][0] if leaks else "a recent data breach"

    template = random.choice(TEMPLATES)
    return template.format(name=name, job=job, company=company, leak=leak)
