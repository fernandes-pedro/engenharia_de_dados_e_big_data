from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv
load_dotenv()

uri = f"mongodb+srv://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@cluster0.4nyq1i4.mongodb.net/?appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))

db = client['sample_mflix'] 
print(db)
collection = db['movies']
print(collection)