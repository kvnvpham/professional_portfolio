from flask import Flask, render_template
from datetime import date
import json

app = Flask(__name__)


@app.route("/")
def home():
    with open("data.json") as file:
        data = json.load(file)

    return render_template("index.html", projects=data)


@app.context_processor
def inject_copyright():
    return {"year": date.today().year}


if __name__ == "__main__":
    app.run()
