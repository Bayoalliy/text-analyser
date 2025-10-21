from dotenv import load_dotenv
import os
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()

# Access them
db_url = os.getenv("DATABASE_URL")

client = MongoClient(db_url)
try:
    # Check the connection by listing database names
    print(client.list_database_names())
except Exception as e:
    print(e)
