from pymongo import MongoClient
import configparser
import os

_config = configparser.ConfigParser()
_credentials_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "credentials.ini")
_config.read(_credentials_path)

_mongo_uri = _config.get("mongo", "URI", fallback="mongodb://localhost:27017")
_db_name = _config.get("mongo", "DB_NAME", fallback="recipes_db")

_client = MongoClient(_mongo_uri)
_db = _client[_db_name]

def get_favorites_collection():
    return _db["favorites"]