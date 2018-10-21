#importing flask and render templates so we can use flask.
from flask import Flask, render_template

#setting up our app.
app = Flask(__name__)

# Setting up our first route,
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/show')
def show():
	return render_template('show.html')

@app.route('/success')
def success():
	return render_template('success.html')

@app.route('/contact_us')
def contact_us():
	return render_template('contact_us.html')

# To check our page and run our app to launch our local host.
if __name__ == '__main__':
	app.debug = True
	app.run()
