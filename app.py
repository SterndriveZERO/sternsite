from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/pvp")
def pvp():
    return render_template("pvp.html")


@app.route("/pvp/beginner")
def beginner():
    return redirect(url_for("beginner_settings"))


@app.route("/pvp/beginner/settings")
def beginner_settings():
    return render_template("pvp/beginner/settings.html")


@app.route("/pvp/beginner/mods")
def beginner_mods():
    return render_template("pvp/beginner/mods.html")


@app.route("/pvp/beginner/texture-packs")
def beginner_texture_packs():
    return render_template("pvp/beginner/texture-packs.html")


@app.route("/pvp/beginner/tips")
def beginner_tips():
    return render_template("pvp/beginner/tips.html")


@app.route("/sword")
def sword():
    return render_template("sword.html")

@app.route("/sword/basic")
def basic():
    return render_template("sword/basic.html")

@app.route("/sword/intro")
def intro():
    return render_template("sword/intro.html")

@app.route("/sword/core")
def core():
    return render_template("sword/core.html")

@app.route("/sword/intermediate")
def intermediate():
    return render_template("sword/intermediate.html")

@app.route("/sword/combo")
def combo():
    return render_template("sword/combo.html")

@app.route("/sword/defense")
def defense():
    return render_template("sword/defense.html")

@app.route("/sword/advanced")
def advanced():
    return render_template("sword/advanced.html")

@app.route("/sword/counters")
def counters():
    return render_template("sword/counters.html")

@app.route("/sword/playstyle")
def playstyle():
    return render_template("sword/playstyle.html")

@app.route("/sword/sweeps")
def sweeps():
    return render_template("sword/sweeps.html")

@app.route("/sword/skills")
def skills():
    return render_template("sword/skills.html")
    
if __name__ == "__main__":
    app.run(debug=True)