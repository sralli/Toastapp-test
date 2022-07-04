import pymongo
from toast_app import connect_mongo
import pandas as pd


client = connect_mongo()
collection = client['Inventory']['menu']

overall_cart = {} #This should be a database entry


def cart(item_id, operation, user_id, overall_cart):
    '''
        Given an item id, perfrom the operation on item wrt cart. 
        item_id: int
        operation: from any one ['Add', 'Remove']
        user_id: The user who is performing the order
        cart, current cart of the user
        overall_cart: this acts as the cart for all the user orders. Temporary solution
    '''

    

    item = collection.find_one(
        {'item_id': item_id}, {'Item name': 1, 'Restaurant': 1, 'Price': 1}
    )

    user_cart = cart_actions(item, user_id, item_id, operation, overall_cart)

    return user_cart, overall_cart

#Helper functions for this function only
        

def cart_actions(item, user_id, item_id, operation, overall_cart):
    if user_id in overall_cart: 
        current_cart = overall_cart[user_id]
    else:
        current_cart = {}

    if operation == 'Add':
        if item_id not in current_cart: 
            # item['quantity'] = 1
            print(item)
            current_cart[item_id] = {'Name': item['Item name'], 'Restaurant':  item['Restaurant'], 'Price': item['Price'], 'Quantity': 1}
        
        else: 
            current_cart[item_id]['Quantity'] = current_cart[item_id]['Quantity']+1
    
    if operation == 'Remove': 

        if item_id not in current_cart:
            raise("This item is not in cart")
        else:
            current_cart[item_id]['Quantity'] = current_cart[item_id]['Quantity']-1

            if current_cart[item_id]['Quantity']==0:
                item_id = current_cart.pop(item_id)

    
    overall_cart[user_id] = current_cart

    return current_cart, overall_cart
  




if __name__ == '__main__':
    cart(1, 'Add', 1)
    print(overall_cart)
    cart(2, 'Add', 1)
    print(overall_cart)

    cart(2, 'Remove', 1)

    print(overall_cart)