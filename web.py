from flask import Flask, render_template, redirect, url_for

app = Flask("beercounter")

COUNTER = 0


def increase_counter(inc=1):
    global COUNTER
    COUNTER += inc


@app.route("/")
def index():
    return render_template("index.html", count=COUNTER, title="Beer Counter")


@app.route("/increase", methods=['POST'])
def increase():
    increase_counter()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
