from flask import Flask, flash, render_template, request

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]

@app.route('/')
def index():
	"""Index page"""
	pass

if __name__ == '__main__':
    app.run()