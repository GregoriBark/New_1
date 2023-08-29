from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start_page():
    return render_template("start_page.html")


@app.route('/main')
def main_page():
    return 'main_page'


if __name__ == "__main__":
    app.run()
