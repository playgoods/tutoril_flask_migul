from flask import Flask
from flask.ext.script import Manager

app = Flask(__name__)

manger = Manager(app)

@app.route('/')
def index():
	return "hello world good time who are you "
	
if __name__ == "__main__":
	manger.run()
