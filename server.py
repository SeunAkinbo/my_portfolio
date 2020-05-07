from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/<string:html_page>')
def index_page(html_page):
    return render_template(html_page)


def write_to_file(data):
    with open('database.txt', mode='a+') as database:
        email = data['Email']
        subject = data['Subject']
        message = data['Message']
        database.write(f'\n{email}\n{subject}\n{message}\n')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        email = data['Email']
        subject = data['Subject']
        message = data['Message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something Went Wrong!!!'