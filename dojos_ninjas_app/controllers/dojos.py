from flask import render_template, request, redirect, session

from dojos_ninjas_app import app

# import the class from friend.py
from dojos_ninjas_app.models.dojo import Dojo


@app.route("/dojos")
def dojo():
    # call the get all classmethod to get all dojos
    dojos = Dojo.get_all()
    return render_template("Dojos.html", all_dojos=dojos)


@app.route('/dojos/<int:id>')
def show_dojos(id):
    data = {
        'id': id
    }
    dojo = Dojo.get_one(data)
    return render_template('NinjasInDojo.html', dojo=dojo)


@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    data = {
        'dojo_name': request.form['dojo_name']
    }
    Dojo.create_new(data)
    return redirect('/dojos')
