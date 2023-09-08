from os import getenv
import socket
from flask import Flask,request,render_template, redirect, make_response 
from dbm import Dbm 
from utils import *

app = Flask(__name__)
base_url = getenv("BASE_URL",default=f"http://{socket.gethostbyname(socket.gethostname())}:5000")

database = Dbm()
database.init()

@app.route("/") #homepage
def home():
    r = render_template("index.html",url=request.url,title="Clickstat - A URL shortner with IP and GPS loging",description="Clickstat is a URL shortener with IP and location tracking capabilities. Shorten your links with Clickstat, and you will be able to view information about those who click on it. This information includes IP address, GPS location, User-Agent, and more. Unlike other services, Clickstat uses GPS to log the location for pinpoint accuracy. Experience the most feature-packed URL shortener with Clickstat.")
    return r

@app.route("/createlink",methods=["POST"]) # this end point is used by the form in the home page to generate shor urls
def createlink():
    ip = get_client_ip(request)
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
    return render_template("show_link.html",link=base_url+f"/{identifier}",identifier=identifier)

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
        ip = get_client_ip(request) 
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
            ip = get_client_ip(request) 
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
        return render_template("404.html",utl=request.url, title="404 Not Found",description="404 Not Found")
@app.route("/stats",methods=["GET","POST"])
def stats():
    if request.method == "POST":
        identifier = request.form["identifier"]
        db = Dbm()
        result = db.get_stats(identifier)
        if result:
            click_stats = parse_and_format(result)
            return render_template("show_stats.html", identifier=identifier, data=click_stats) 
        else:
            return render_template("unavailable.html") 
    else:
        return render_template("stats.html",url=request.url,title="Stats - View data about your shortened links.",description="You can view information about your shortened links on this page.")

@app.route("/about")
def about():
    return render_template("about.html",url=request.url,title="About Clickstat",description="Clickstat is a URL shortener with IP and location tracking capabilities. Shorten your links with Clickstat, and you will be able to view information about those who click on it. This information includes IP address, GPS location, User-Agent, and more. Unlike other services, Clickstat uses GPS to log the location for pinpoint accuracy. Experience the most feature-packed URL shortener with Clickstat.")
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
