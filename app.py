from flask import Flask, render_template, request
from utils import process_candidates
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    if request.method == "POST":
        jd = request.form["jd"]
        results = process_candidates(jd)
    return render_template("index.html", results=results)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # important for deployment
    app.run(host="0.0.0.0", port=port)