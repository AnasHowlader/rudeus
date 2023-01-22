from flask import Blueprint, render_template, jsonify, request, redirect, url_for

routes = Blueprint("routes", __name__)

@routes.route('/')
def home():
    return render_template("base.html",name="Jion")

@routes.route('/test/<username>')
def test(username):
    return render_template("base.html",name=username)

@routes.route("/json")
def get_json():
    return jsonify({'name':'kaka'})

@routes.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@routes.route("/go-to-home")
def go_home():
    return redirect(url_for("routes.get_json"))

@routes.route("newpage")
def newpage():
    return render_template("newpage.html")

@routes.route("testpage")
def testpage():
    return render_template("testpage.html")