from flask import Flask,request,render_template
app = Flask(__name__)

@app.route("/")
def home():
    r = render_template("index.html")
    return r
@app.route("/getlink",methods=["POST"])
def data():
    data = request.json
    print(data)
    linkData = {"link" : "https://google.com"}
    return linkData


if __name__ == "__main__":
    app.run(debug=True)
