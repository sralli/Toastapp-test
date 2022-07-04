from toast_app import connect_mongo
from pymongo import MongoClient

def test_connect_mongo():
    mongo = connect_mongo()
    assert  MongoClient == type(mongo)