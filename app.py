from flask import Flask,request,render_template, redirect
from dbm import Dbm, command
from utils import generate_identifier 

app = Flask(__name__)
base_url = "http://localhost:5000"

database = Dbm()
database.init()

@app.route("/") #homepage
def home():
    r = render_template("index.html")
    return r

@app.route("/createlink",methods=["POST"]) # this end point is used by the form in the home page to generate shor urls
def createlink():
    # ip = request.remote_addr # this will not work if you're using a load balancer which you should
    ip = request.headers.get('X-Forwarded-For', request.remote_addr) # works if the flask app is running behind a load balancer
    url = request.form["url"]
    if "enable" in request.form:
        TL = 1
    else:
        TL = 0
    while True:
        try:
            identifier = generate_identifier()
            data = {"url":url,"identifier":identifier, "TL":TL, "owner_ip":ip}
            database = Dbm()
            database.generate_link(data)
            break
        except:
            continue
    return render_template("show_link.html",link=base_url+f"/{identifier}")

@app.route("/getlink",methods=["POST"]) #this route is used by the js that sends the gps data
def data():
    data = request.json
    print(data)
    linkData = {"link" : "https://google.com"}
    return linkData

@app.route("/<identifier>",methods=["GET"])
def fetchURL(identifier):
    db = Dbm()
    link = db.fetch_link(identifier)
    return redirect(link,code=302) 

if __name__ == "__main__":
    app.run(debug=True)
