import os
import pymongo

client = pymongo.MongoClient(os.envrion('MONGO_CONN'))
# db = client.test

def get_document():
    return None