
from pymongo import MongoClient


from src.config.constants import MONGO_URI

client = MongoClient(MONGO_URI)

db_mongo = client['test']



