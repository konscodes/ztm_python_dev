from flask import Flask, render_template

app = Flask(__name__)
print(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/home')
def home_index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/components')
def components():
    return render_template('components.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/download')
def download():
    return render_template('download.html')


@app.route('/pricing')
def pricing():
    return render_template('pricing.html')