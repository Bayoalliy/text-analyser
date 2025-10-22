from dotenv import load_dotenv
import os
from pymongo import MongoClient
load_dotenv()

class DBstorage():
	def __init__(self):
		self.db_url = os.getenv("DATABASE_URL")
		self.client = MongoClient(self.db_url)
		self.db = self.client['hng-task_1']

	def save(self, obj):
		res = self.db.strings.insert_one(obj)
		return res.inserted_id

	def find_string(self, obj):
		return self.db.strings.find_one(obj)
	
	def find_all(self, filters):
		return self.db.strings.find(filters)
