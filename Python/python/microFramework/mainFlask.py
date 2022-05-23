
from flask import Flask, render_template, request

app = Flask("MyFlaskApp", static_folder="static")


@app.route('/')
def Hello():
    return 'Hello World!'


@app.route('/sample')
def getSampleHtml():
    return render_template('sample.html')


if __name__ == '__main__':
    app.run(debug=True, port=5555)
