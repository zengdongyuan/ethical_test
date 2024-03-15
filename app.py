
from flask import Flask,request,render_template
app = Flask(__name__)

name_flag=0
name=""

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    global name_flag
    if name_flag==0:
        name = request.form.get("name")
        name_flag=1
    return(render_template("main.html", name=name))
@app.route("/ethical_test",methods=["GET","POST"])
def ethical_test():
    return(render_template("ethical_test.html"))

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
