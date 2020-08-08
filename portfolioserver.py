import os, json, csv
from flask import Flask, render_template, url_for, send_from_directory,request, redirect
app = Flask(__name__)
print(__name__)

#
# app.add_url_rule('/favicon.ico',
#                  redirect_to=url_for('static', filename='favicon.ico'))
@app.route('/')
def home_page():
    return render_template('index.html')
@app.route('/<string:page_name>')
def page_name(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)

            # request.form['subject']
            # request.form['message']
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'

def write_to_file(data):
    with open('database.txt', mode='a') as my_file:
        email = data['email']
        subject = data['subject']
        message = data['message']

        my_file.write(f'\nFROM: {email}, \n SUBJECT: {subject},\n\n{message}')
        print('wykonano')
def write_to_csv(data):
    with open('database.csv', mode='a') as csv_file:
        email = data['email']
        subject = data['subject']
        message = data['message']

        csv_writer=csv.writer(csv_file, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
        print('wykonano')
 # with open('database.txt', mode='w') as my_file:
 #            # out1=' '
 #            # out1 =out1.join(data1)
 #            my_file.write(json.dumps(data))
 #            print('wykonano')


#
# @app.route('/about.html')
# def about ():
#     return render_template('about.html')
#
# @app.route('/services.html')
# def services ():
#     return render_template('services.html')
#
#
# @app.route('/contact.html')
# def contact ():
#     return render_template('contact.html')
#
# @app.route('/components.html')
# def components ():
#     return render_template('components.html')



@app.route('/<username>/<int:post_id>')
def name_name(username,post_id):
    #username=username
    return render_template('web.html',name=username,post_id=post_id)

# @app.route('/favicon.ico')
# def faviicon():
#     return send_from_directory('static/favicon.ico',
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')
