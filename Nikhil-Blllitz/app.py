from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')

def index():
    return render_template('base.html')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html')
if __name__ == "__main__":
    app.run(debug=True)