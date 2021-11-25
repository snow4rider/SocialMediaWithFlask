from flask import Flask, render_template
from flask_navigation import Navigation
#from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__) 
nav = Navigation(app)

nav.Bar('top',[
  nav.Item('Home', 'index'),
  nav.Item('contact', 'contact'),
  nav.Item('about-me', 'about_me'),
])


@app.route("/")
def index():
  return render_template('index.html')
 

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/about-me')
def about_me():
  return render_template('about_me.html')


app.run(host='0.0.0.0', port=5000, debug=True)  # Run the Application (in debug mode)
