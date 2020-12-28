from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    current_year = datetime.datetime.now().year
    print(current_year)
    return render_template('index.html', year=current_year)


if __name__ == '__main__':
    app.run(debug=True)
