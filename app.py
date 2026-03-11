from flask import Flask, render_template

print("APP FILE LOADED")

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/loginpage")
def loginpage():
    return render_template("loginpage.html")

@app.route("/resultpage")
def resultpage():
    return render_template("resultpage.html")

@app.route("/test")
def test():
    return "Flask routing works!"

if __name__ == "__main__":
    app.run(debug=True)