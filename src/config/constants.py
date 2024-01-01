import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')

API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')

HEADERS = {"Authorization": f"Bearer {API_KEY}"}

API_URL_GOOGLE = BASE_URL + 'google/vit-base-patch16-224'
API_URL_MICROSOFT = BASE_URL + 'microsoft/resnet-50'