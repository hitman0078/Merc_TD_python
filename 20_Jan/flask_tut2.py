from flask import Flask
  
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask!"

@app.route("/test")
def test():
    return "Test Method!"

@app.route("/nums")
def nums():
    nums=[10,20,30]
    return nums


@app.route("/displayItems")
def display_food_items():
    food_items=[Food(101,"burger",100),Food(102,"pizza",200)]
    return food_items

@app.route("/displayFood")
def display_food():
    return Food(101,"burger",100)

if __name__ == "__main__":
    app.run(debug=True)
