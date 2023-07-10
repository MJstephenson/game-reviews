import os, json
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env




app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/get_add_game")
def get_add_game():
    add_game = mongo.db.add_game.find()
    return render_template("add_game.html", add_game=add_game)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))

            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # this will get the users username from the database
    username = mongo.db.users.find_one(
        {"username":session["user"]})["username"]

    if session['user']:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # this will remove user from session cookies when they log out
    flash("you have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_review", methods=['GET','POST'])
def add_review():
    if request.method == 'POST':
        review = {
            'game_name': request.form.get('game_name'),
            'publisher': request.form.get('publisher'),
            'developer': request.form.get('developer'),
            'release_year': request.form.get('release_year'),
            'genre': request.form.get('genre'),
            'player_number': request.form.get('player_number'),
            'game_review': request.form.get('game_review'),
        }
        mongo.db.add_review.insert_one(review)
        flash('Review successfully added')
        
    with open('data/games.json') as f:
        games = json.load(f)
    game_names = [game['Game'] for game in games]
    return render_template("add_review.html", game_names=game_names)


@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/database")
def database():
    return render_template("database.html")


@app.route("/reviews")
def reviews():
    add_game = mongo.db.add_game.find()
    return render_template("reviews.html", add_game=add_game)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
            