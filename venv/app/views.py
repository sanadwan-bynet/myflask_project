from datetime import datetime
from turtle import title

from flask import Flask, render_template
from app.attendance_processer.parse_attendance import my_attendance
from . import app


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )
@app.route('/attendance')
def attendance():
    data = my_attendance()
    titles = data.columns.values
    data = data.to_html(classes='data')
	
    return render_template('attendance.html', tables = [data], titles=title)

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
