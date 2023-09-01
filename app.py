from flask import Flask,request,render_template

from dbm import Dbm 

#this functino reads the .sql files content and returns it as string
def sql(filename):
    with open("sql/"+filename,"r") as f:
        query = f.read()
        return query

#creating the database if it already dosn't exist
database = Dbm()
database.execute(sql_command=sql("create_links.sql"))
database.execute(sql_command=sql("create_data.sql"))

app = Flask(__name__)

@app.route("/")
def home():
    r = render_template("index.html")
    return r
@app.route("/createlink",methods=["POST"])
def createlink():
    url = request.form["url"]
    return render_template("show_link.html",link=url)
@app.route("/getlink",methods=["POST"])
def data():
    data = request.json
    print(data)
    linkData = {"link" : "https://google.com"}
    return linkData


if __name__ == "__main__":
    app.run(debug=True)
