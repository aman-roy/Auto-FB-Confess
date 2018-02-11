import os

from flask import Flask, flash, render_template, request
from helpers import *


app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]

@app.route('/')
def index():
	"""Index page"""
	if request.method == "POST":
		msg = request.form.get("textarea")
		if msg:
			fbpost(msg)
			flash('Successfully posted!')

	return render_template('index.html', name=os.environ["NAME"])


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, unexpected error: {}'.format(e), 404	

@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500

if __name__ == '__main__':
    app.run()