from flask import Flask, request, jsonify
from dbconnection import supabase
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort
from decimal import Decimal
from datetime import datetime

def valid_datetime(value):
    try:
        return datetime.fromisoformat(value)
    except ValueError:
        raise ValueError("Invalid datetime format, use YYYY-MM-DDTHH:MM:SS")
app = Flask(__name__)
api = Api(app)

#buat ngecek data (?) flask parser BUAT POST DOANG BUTUH
user_args = reqparse.RequestParser()
user_args.add_argument("email", type = str, required = True, help='email tidak boleh kosong')
user_args.add_argument("password", type = str, required = True, help='password tidak boleh kosong')

orderitem_args = reqparse.RequestParser() # -> optional sebenermya cuma butuh kalo frontend send product + quantity langsung
orderitem_args.add_argument("order_id", type=int, required=True, help="order_id harus di isi")
orderitem_args.add_argument("product_id", type=int, required=True, help="product_id harus di isi")
orderitem_args.add_argument("quantity", type=int, required=True, help="jumlah produk harus di isi")
orderitem_args.add_argument("total_price", type=Decimal, required=False, help="boleh kosong, bisa dihitung otomatis")

cart_args = reqparse.RequestParser()
cart_args.add_argument("user_id", type=int, required=True, help="user_id harus di isi")
cart_args.add_argument("product_id", type=int, required=True, help="product_id harus di isi")
cart_args.add_argument("quantity", type=int, required=True, help="jumlah produk harus di isi")
cart_args.add_argument("total_price", type=Decimal, required=False, help="boleh kosong, bisa dihitung otomatis")

order_args = reqparse.RequestParser()
order_args.add_argument("user_id", type=int, required=True, help="user_id harus di isi")


#home page
@app.route('/')
def home():
    return '<h1> Tugas Ecommerce Supabase API</h1>'

#ambil data produk
class product(Resource):

    def get(self):
        response = supabase.table("products").select("*").execute()
        return jsonify(response.data)

api.add_resource(product, "/api/products")


#operasi users
class users(Resource):
    def get(self):
        response = supabase.table("users").select("*").execute()
        return jsonify(response.data)

    #insert data user
    def post(self):
        args = user_args.parse_args()
        response = (supabase.table("users").insert({"email": args["email"], "password": args["password"]}).execute())
        return jsonify(response.data), 201

api.add_resource(users, "/api/users")

#operasi cart
class cart(Resource):
    def get(self):
        response = supabase.table("cart").select("*").execute()
        return jsonify(response.data)
    
    def post(self):
        args = cart_args.parse_args()
        response = (supabase.table("cart").insert({"user_id": args["user_id"], "product_id": args["product_id"], "quantity": args["quantity"]}).execute())
        return jsonify(response.data), 201

api.add_resource(cart, "/api/cart")

#operasi orders
class orders(Resource):
  def get(self):
        response = supabase.table("orders").select("*").execute()
        return jsonify(response.data)
  def post(self):
        args = order_args.parse_args()
        response = (supabase.table("orders").insert({"user_id": args["user_id"]}).execute())
        return jsonify(response.data), 201


api.add_resource(orders, "/api/orders")

#operasi order_items
class order_items(Resource):
    def get(self):
        response = supabase.table("order_items").select("*").execute()
        return jsonify(response.data)
    
api.add_resource(order_items, "/api/order_items")

if __name__ == "__main__":
    app.run(debug=True)