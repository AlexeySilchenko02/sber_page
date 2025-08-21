from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello</h1>"

@app.route('/string-sum')
def string_sum():
    return render_template('string_sum.html')

@app.route('/stat-weekend')
def stat_weekend():
    return render_template('stat_weekend.html')

if __name__ == '__main__':
    app.run(debug=True)