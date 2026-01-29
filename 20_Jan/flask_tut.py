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
@app.route("/set")
def nums1():
    nums1 = {1:"hello",2:"hi"}
    return nums1
 
if __name__ == "__main__":
    app.run(debug=True)


