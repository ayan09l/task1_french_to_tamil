from flask import Flask, render_template, request
from model import FrenchToTamilTranslator

app = Flask(__name__)
translator = FrenchToTamilTranslator()

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    word = ""

    if request.method == "POST":
        word = (request.form.get("word") or "").strip()
        output = translator.translate(word)

    # render same page with word and output (keeps user on App)
    return render_template("index.html", output=output, word=word)

if __name__ == "__main__":
    app.run(debug=True)
