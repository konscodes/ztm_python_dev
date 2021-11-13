from flask import Flask, render_template, request
from pathlib import Path
import csv

script_path = Path(__file__).resolve()
script_parent = script_path.parent
data_file_path = script_parent / 'database.csv'
app = Flask(__name__)

def append_new_line(file_path, what_to_append):
    with open(file_path, 'a') as file_object:
        name = what_to_append['name']
        email = what_to_append['email']
        subject = what_to_append['subject']
        message = what_to_append['message']
        csv_writer = csv.writer(file_object)
        csv_writer.writerow([name, email, subject, message])

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


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        append_new_line(data_file_path, data)
        return render_template('submitted.html')
    else:
        return 'Something went wrong.. Try again.'