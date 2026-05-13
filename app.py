from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/pvp")
def pvp():
    return render_template("pvp.html")

@app.route("/sword")
def sword():
    return render_template("sword.html")

@app.route("/crystal")
def crystal():
    return render_template("crystal.html")

@app.route("/smp")
def smp():
    return render_template("smp.html")

@app.route("/uhc")
def uhc():
    return render_template("uhc.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)