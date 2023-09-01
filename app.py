from flask import Flask,request,render_template, redirect, make_response, jsonify
from dbm import Dbm 
from utils import *

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

    if not data:
        return make_response("Bad request",400)
    db = Dbm()
    result = db.fetch_link(data["identifier"])
    if result:
        link = result[0][0]
        linkData = {"link" : link}
        #collect data
        ip = request.headers.get('X-Forwarded-For', request.remote_addr) 
        user_agent = request.headers.get('User-Agent')
        data["user_agent"]=user_agent
        data["ip"]=ip
        db = Dbm()
        db.insert_into_data(data)
        return linkData
    else:
        return "url doesn't exist"

@app.route("/<identifier>",methods=["GET"])
def fetchURL(identifier):
    db = Dbm()
    result = db.fetch_link(identifier)
    if result:
        if result[0][1] == 0:
            ip = request.headers.get('X-Forwarded-For', request.remote_addr)
            user_agent = request.headers.get('User-Agent')
            data = {
                "identifier": identifier,
                "ip": ip,
                "user_agent": user_agent,
                "latitude": None,
                "longitude": None 
            }
            db = Dbm()
            db.insert_into_data(data)
            return redirect(result[0][0],code=302) 
        elif result[0][1] == 1:
            return render_template("locate.html",identifier=identifier)
    else:
        return "<h1>404 Not found</h1>"
@app.route("/stats=<identifier>")
def stats(identifier):
    db = Dbm()
    result = db.get_stats(identifier)
    if result:
        click_stats = parse_and_format(result)
        return render_template("show_stats.html",data=click_stats) 
    else:
        return "<h1>No clicks yet.</h1>"

if __name__ == "__main__":
    app.run(debug=True)
