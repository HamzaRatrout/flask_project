from flask import Flask, render_template, request
import random 
quote= ["<h1>Live more Worry less</h1>","<h1>Don't dream for success work for it</h1>","<h1>Beauty is a power a smile is its sword</h1>","<h1>When it rains look for rainbow</h1>","<h1>Good vibes only</h1>"]

app = Flask(__name__)
@app.route("/rnd")
def randomq():
	rand_item = quote[random.randrange(len(quote))]
	return (rand_item)
@app.route("/")
def hi():
	return render_template("mypage.html")

#change
@app.route("/pick")
def load_page():
	return render_template("mypage2.html")
@app.route("/about")
def load_page1():
	return render_template("aboutme.html")
@app.route("/hob")
def load_page2():
	return render_template("hobbies.html")
@app.route("/aboutme2")
def load_page43():
	return render_template("aboutme2.html")
@app.route("/form")
def load_page3():
	return render_template("form.html")

@app.route("/sign" ,methods = ['POST' , 'GET'])
def load_page4():
	firstname = request.form['firstname']
	lastname = request.form['lastname']
	email = request.form['email']
	return render_template('result.html' ,firstname = firstname , lastname = lastname , 
	email = email ) 

if __name__ == "__main__":
	app.run()
