from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def welcome():
    #return 'Welcome to Heng Online Store!'
    return render_template('index.html')

# Calling the page dynamicaly 
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)    

def write_to_db(data):
    pass

def write_to_csv(data):
    with open('database.csv', 'a', newline='') as csv_db:
        email = data['email']
        subject = data['subject']
        msg = data['message']
        csv_writer = csv.writer(csv_db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, msg])


@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        # with open ('database.txt', mode='a') as db:
        #    _file = db.write(f'\n{data["email"]},{data["subject"]},{data["message"]}')
        return redirect('thankyou.html')
    else:
        'Something went wrong!! Please try again.'

# @app.route('/index.html')
# def home():
#     #return 'Welcome to Heng Online Store!'
#     return render_template('index.html')

# @app.route('/works.html')
# def work():
#     #return 'Welcome to Heng Online Store!'
#     return render_template('works.html')

# # @app.route('/<username>/<int:post_id>')
# # def welcome_user(username=None, post_id=None):
# #     #return 'Welcome to Heng Online Store!'
# #     return render_template('index.html', name=username, post_id=post_id)

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')

# # @app.route('/blog')
# # def blog():
# #     return 'This page contains blog post'
    
# @app.route('/blog/2020/dog')
# def blog_dog():
#     return 'Blogs about dog'
