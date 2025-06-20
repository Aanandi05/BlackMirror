import os
from dotenv import load_dotenv

load_dotenv()

SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
USE_SERPAPI = os.getenv("USE_SERPAPI", "False").lower() == "true"
