from flask import Flask,render_template
import pandas as pd
app =Flask('Website')

@app.route("/")
def home():
    return render_template("home.html")
app.run(debug=True)