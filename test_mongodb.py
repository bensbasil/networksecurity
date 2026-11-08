import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

if not MONGO_DB_URL:
    raise ValueError("MONGO_DB_URL is missing from environment variables")

client = MongoClient(MONGO_DB_URL)

try:
    client.admin.command("ping")
    print("Connected successfully")

except Exception as e:
    raise Exception(f"The following error occurred: {e}") from e

finally:
    client.close()
