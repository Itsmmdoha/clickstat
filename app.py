from flask import Flask,request,render_template,redirect
app = Flask(__name__)

@app.route("/")
def home():
    r = render_template("index.html")
    return r
@app.route("/data",methods=["POST"])
def data():
    pass


if __name__ == "__main__":
    app.run(debug=True)
