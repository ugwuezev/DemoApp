from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
{
	'author': 'Vincent Davince',
	'title': 'Blog Post 1',
	'content': 'First Content',
	'date_posted': 'April 24, 2012'
},
{
	'author': 'Victor Vinny',
	'title': 'Blog Post 2',
	'content': 'Second Content',
	'date_posted': 'March 4, 2018'
}
]


@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html', title='About')





if __name__ == '__main__':
	app.run(debug=True)	
