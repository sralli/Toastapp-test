from flask import Flask, request
from toast_app import load_menu, cart
import json

app = Flask(__name__)

#global variables 
global overall_cart
overall_cart = {}

@app.route('/menu/load_menu', methods=['GET', 'POST'])
def load_user_menu():
    if request.method == 'GET':
        return load_menu(None, None)
    if request.method == 'POST':
        restaurant_name = request.form.get('restaurant_name')
        category_name = request.form.get('category_name')

        menu = load_menu(restaurant_name, category_name)
        print(restaurant_name)
        print(category_name)

        return json.dumps(menu)


@app.route('/menu/cart_action', methods=['POST'])
def update_cart():
    global overall_cart
    if request.method == 'POST':
        item_id = request.form.get("item_id")
        operation = request.form.get("operation")
        user_id = request.form.get("user_id")
        user_cart, overall_cart_updated  = cart(int(item_id), operation, user_id, overall_cart)
        print(user_cart)
        overall_cart = overall_cart_updated
        return user_cart


if __name__ == '__main__':
    app.run()