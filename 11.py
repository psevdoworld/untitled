from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("main.html")

@app.route("/<name>")
def hello_by_name(name):
    return render_template("hello.html", name=name)
    
@app.route("/рш")
def rsh():
    name = request.args.get('name','')
    return hello_by_name(name)
if __name__ == "__main__":
    app.run()
