from flask import render_template, url_for

def login():
    return render_template("auth/login.html")             
