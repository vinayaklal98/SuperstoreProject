from flask import Flask, jsonify, request

app = Flask(__name__)

items = [{"category":"electronics","name":"OnePlus 7t","brand":"OnePlus","price":"Rs. 38999"},
{"category":"grocery","name":"Amul Tonned Milk","brand":"Amul India","price":"Rs. 38"},
{"category":"clothing","name":"Raymond Slim-fit Shirt","brand":"Raymond Clothing","price":"Rs. 8999"},
{"category":"clothing","name":"UCLA Yellow Tshirt","brand":"UCLA Clothing","price":"Rs. 999"}]


@app.route("/")
def hello():
	return jsonify({"about":"Hello This is API Demo"})

@app.route("/superstore/signup",methods=['GET', 'POST'])
def signup():
	if request.method == 'POST':
		msg = request.get_json()
		return jsonify({"GOT POST":msg}),201
	else:
		return jsonify({"error":"Got Error"}),404

@app.route("/superstore/login", methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		msg = request.get_json()
		print(msg)
		if msg['username'] == 'test' and msg['password'] == 'test@123':
			return jsonify({"GOT POST":"login successful!!"}),200
	else:
		return jsonify({"error":"Got Error"}),404

@app.route("/superstore/category/electronics",methods=['GET', 'POST'])
def catelec():
	sent = []
	if request.method == 'POST':
		msg = request.get_json()
		for index in range(len(items)):
			if msg['name'] == items[index]['name']:
				sent.append(items[index])
		return jsonify({"GOT GET":sent}),200
	elif request.method == 'GET':
		for index in range(len(items)):
			if items[index]['category'] == 'electronics':
				sent.append(items[index])
		msg = request.get_json()
		return jsonify({"GOT GET":sent}),200
	else:
		return jsonify({"error":"Got Error"}),404

@app.route("/superstore/category/grocery",methods=['GET', 'POST'])
def catgroc():
	sent = []
	if request.method == 'POST':
		msg = request.get_json()
		for index in range(len(items)):
			if msg['name'] == items[index]['name']:
				sent.append(items[index])
		return jsonify({"GOT GET":sent}),200
	elif request.method == 'GET':
		for index in range(len(items)):
			if items[index]['category'] == 'grocery':
				sent.append(items[index])
		msg = request.get_json()
		return jsonify({"GOT GET":sent}),200
	else:
		return jsonify({"error":"Got Error"}),404

@app.route("/superstore/category/clothing",methods=['GET', 'POST'])
def catcloth():
	sent = []
	if request.method == 'POST':
		msg = request.get_json()
		for index in range(len(items)):
			if msg['name'] == items[index]['name']:
				sent.append(items[index])
		return jsonify({"GOT GET":sent}),200
	elif request.method == 'GET':
		for index in range(len(items)):
			if items[index]['category'] == 'clothing':
				sent.append(items[index])
		msg = request.get_json()
		return jsonify({"GOT GET":sent}),200
	else:
		return jsonify({"error":"Got Error"}),404
