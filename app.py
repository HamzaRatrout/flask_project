from flask import Flask, render_template
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


@app.route("/pick")
def load_page():
	return render_template("mypage2.html")
	
if __name__ == "__main__":
	app.run()
