import pymongo
import pandas as pd
from toast_app import connect_mongo
import json

def import_data(db_name, collection_name, path_name = None):
    '''
        Function to read the csv and import data. 
        For resuability 
            1. Add path name 
    '''
    client = connect_mongo()
    db = client[db_name]
    coll = db[collection_name]
    if path_name==None:
        data = pd.read_csv('/home/shivam/Desktop/Projects/toastapp/toast_app/menu_items/import_data/Menu items - Sheet1.csv')
    else:
        data = pd.read_csv(path_name)

    payload = json.loads(data.to_json(orient='records'))
    coll.remove()
    coll.insert(payload)
    return coll.count()


if __name__ == "__main__":
    import_data('Inventory', 'menu')