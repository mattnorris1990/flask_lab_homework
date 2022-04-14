from flask import render_template
from app import app
from models.order_list import order_list

@app.route("/")
def home():
    return "THE BOOK SHOP"

@app.route("/orders")
def index():
    return render_template('index.html', title="Book Shop", orders = order_list)

@app.route("/orders/<element>")
def order(element):
    return render_template('order.html', title="Book Shop", order = order_list[int(element)])