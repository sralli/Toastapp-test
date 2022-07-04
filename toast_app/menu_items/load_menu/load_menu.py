from toast_app import connect_mongo

def load_menu(restaurant_name=None, category_name=None):
    '''
        A function to load the menu. 
        Default = Load all the menu items
        Category: Load all items for the menu
        Restaurant name: Load all items for the restaurant
    
    '''


    client = connect_mongo()
    loaded_menu = []
    print(restaurant_name, category_name)
    coll = client['Inventory']['menu']
    if restaurant_name and category_name:
        menu_items = coll.find({'Availability': 'Y', 'Restaurant': restaurant_name, 'Category': category_name})
    elif restaurant_name: 
        menu_items = coll.find({'Availability': 'Y', 'Restaurant': restaurant_name}, {})
    elif category_name: 
        menu_items = coll.find({'Availability': 'Y', 'Category': category_name})
    else:
        menu_items = coll.find({'Availability': 'Y'})

   
    for item in menu_items:
        print(item)
        item = coll.find_one({'_id': item['_id']}, 
        {'item_id': 1,'Item name': 1, 'Restaurant': 1, 'Price': 1, 'Category':1}
    )

        loaded_menu.append([item['item_id'], item['Item name'], item['Restaurant'], item['Category'], item['Price']])

    return (loaded_menu )


if __name__ == '__main__':
    loaded_menu = load_menu(restaurant_name='Overnstory')
    print(loaded_menu)