from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello!'

@app.route('/kek')
def kek():
	posts = [
		{
			'title' : 'kek',
			'created' : 'lol',
		},
		{
			'title' : 'erkjb',
			'created' : '1',
		}
	]
	
	return render_template('main.html', posts=posts)

app.run()
