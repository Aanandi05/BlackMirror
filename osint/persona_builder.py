## modules/persona_builder.py
import random

def build_fake_persona(email):
    username = email.split('@')[0]
    locations = ["Mumbai", "Delhi", "Bangalore", "Pune", "Hyderabad"]
    jobs = ["Software Engineer", "Data Analyst", "Product Manager", "Security Researcher"]
    companies = ["TechNova", "ByteWorks", "CyberEdge", "InnovaSoft"]
    interests = ["machine learning", "cybersecurity", "gaming", "photography"]

    persona = {
        "name": username.replace('.', ' ').title(),
        "location": random.choice(locations),
        "job_title": random.choice(jobs),
        "company": random.choice(companies),
        "interests": random.sample(interests, 2)
    }

    return persona



