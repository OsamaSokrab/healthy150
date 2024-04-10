from flask import Flask, jsonify, request
from markupsafe import escape
from flask import render_template
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<username>:<password>@localhost:5432/<database_name>'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

@app.route("/<name>")
def index(name):
	return f"<h1>Welcome to Bizza Rest API Server!</h1>, {escape(name)}"

@app.route("/api/v1/venues")
def venues():
	return jsonify({"id":1,"name":"Auditorium A"}), 404

@app.route("/api/v1/speakers/")
def speakers():
    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    if firstname is not None and lastname is not None:
        return jsonify(message="The speaker's fullname :" +firstname+" "+lastname)
    else:
        return jsonify(message="No query parameters in the url")
    
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
	app.run()
      
