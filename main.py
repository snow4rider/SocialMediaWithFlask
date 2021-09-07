from flask import (
  Flask, render_template
  )
from flask_navigation import Navigation
#from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)  # Create an Instance
nav = Navigation(app)

nav.Bar('top',[
  nav.Item('Home', 'index'),
  nav.Item('contact-me', 'contact_me'),
  nav.Item('about-me', 'about_me'),
])


@app.route("/")
def index():
  return render_template('index.html')
 

@app.route('/contact_me')
def contact_me():
  return render_template('contact_me.html')

@app.route('/about_me')
def about_me():
  return render_template('about_me.html')


app.run(host='0.0.0.0', port=5000,
        debug=True)  # Run the Application (in debug mode)
