
from flask import Flask,request,render_template,Markup
import datetime
import sqlite3
app = Flask(__name__)

name_flag=0
name=""

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    global name_flag, name
    if name_flag==0:
        name = request.form.get("name")
        name_flag=1
        conn = sqlite3.connect("log.db")
        c = conn.cursor()
        timestamp = datetime.datetime.now()
        c.execute("insert into employee (name,timestamp) values(?,?)", (name, timestamp))
        conn.commit()
        c.close()
        conn.close()
    return(render_template("main.html", name=name))


@app.route("/ethical_test",methods=["GET","POST"])
def ethical_test():
    return(render_template("ethical_test.html"))

@app.route("/ethical_test2",methods=["GET","POST"])
def ethical_test2():
    return(render_template("ethical_test2.html"))
@app.route("/query",methods=["GET","POST"])
def query():
    conn = sqlite3.connect("log.db")
    c = conn.execute("select * from employee")
    r = ""
    for row in c:
        r=r+str(row)+"<br>"
    print(r)
    r=Markup(r)
    c.close
    conn.close
    return (render_template("query.html", r=r))
@app.route("/answer",methods=["GET","POST"])
def answer():
    ans = request.form["options"]
    print(ans)
    if ans == "true":
        return(render_template("wrong.html"))
    elif ans == "false":
        return(render_template("correct.html"))


@app.route("/end",methods=["GET","POST"])
def end():
    return(render_template("end.html"))
    
if __name__ == "__main__":
    app.run()
