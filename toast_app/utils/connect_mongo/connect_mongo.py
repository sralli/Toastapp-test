import pymongo
import os

def connect_mongo(url=None):
    '''
        Return the loaded client that gets the mongodb client. 
        Params: 
            URL: If the url is provided, connect with that, else, connect with the env url
        
        Return:
            mongodb client. 
    '''

    if url is None: 
        url = 'mongodb+srv://sralli:ptolemy@cluster0.xhxwmjy.mongodb.net/?retryWrites=true&w=majority'

    client = pymongo.MongoClient(url)
    
    return client