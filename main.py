from flask import Flask

app = Flask(__name__)


@app.route("/")
def start_page():
    return "Hello Flask!"


@app.route('/main')
def main_page():
    return 'main_page'


if __name__ == "__main__":
    app.run()
