from flask import Flask, render_template, request
from utils import process_candidates

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    if request.method == "POST":
        jd = request.form["jd"]
        results = process_candidates(jd)

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)