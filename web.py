from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/union/xx')
def index():
    text = 'abc'
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template("index.html", n1=text, x2=date_str)


if __name__ == "__main__":
    app.run()  #debug=True,host='0.0.0.0',port=5000