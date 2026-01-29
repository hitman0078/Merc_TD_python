from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask!"

@app.route("/foods")
def foods():
    food_items = [
        {"id": 1, "name": "Pizza", "price": 250},
        {"id": 2, "name": "Burger", "price": 150},
        {"id": 3, "name": "Pasta", "price": 200},
        {"id": 4, "name": "Sandwich", "price": 120}
    ]
    return food_items   # Flask will return this as JSON

@app.route("/fooddict")
def fooddict():
    food_items = {
        1: "Pizza",
        2: "Burger",
        3: "Pasta",
        4: "Sandwich"
    }
    return food_items   

if __name__ == "__main__":
     app.run(debug=True)
