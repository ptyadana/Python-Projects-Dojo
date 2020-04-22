from flask import Flask, render_template, request, url_for, redirect
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt',mode='a') as db:
        email=data['email']
        subject=data['subject']
        message=data['message']
        db.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv','a',newline='') as db:
        email=data['email']
        subject=data['subject']
        message=data['message']

        csv_writer = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

        # fieldnames = ['email', 'subject', 'message']
        # writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        # writer.writerow({'email': email, 'subject': subject, 'message':message})

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to Database.'
    else:
        return 'Opps! something went wrong.'