# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import os
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
@app.route("/home")
def home():
    return render_template("home.html", home=home)


@app.route("/get_category", methods=["GET" , "POST"])
def get_category():
    if request.method == "POST":
        recipe = {
            "recipe_category_name": request.form.get("recipe_category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_prep_time": request.form.get("recipe_prep_time"),
            "recipe_ingrediens": request.form.get("recipe_ingrediens"),
            "recipe_preparation": request.form.get("recipe_preparation"),
            "recipe_author_name": session["user"],
            "recipe_img": request.form.get("recipe_img"),
        }
        mongo.db.recipe.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))

    category = list(mongo.db.category.find())
    return render_template("add_recipe.html", category=category)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {
            "recipe_category_name": request.form.get("recipe_category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_prep_time": request.form.get("recipe_prep_time"),
            "recipe_ingrediens": request.form.get("recipe_ingrediens"),
            "recipe_preparation": request.form.get("recipe_preparation"),
            "recipe_author_name": session["user"],
            "recipe_img": request.form.get("recipe_img"),
        }
        mongo.db.recipe.replace_one({"_id": ObjectId(recipe_id)}, submit, True)
        flash("Recipe Successfully Updated")

    recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    category = list(mongo.db.category.find())
    return render_template("edit_recipe.html", recipe=recipe , category=category)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipe.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


@app.route("/get_recipes")
def get_recipes():
    recipe = list(mongo.db.recipe.find())
    return render_template("get_recipes.html", recipe=recipe)


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


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
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
                return redirect(url_for("log_in"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("log_in"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):


    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("log_in"))


@app.route("/log_out")
def log_out():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("log_in"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
