from flask_app import app

from flask import render_template, request, redirect

from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninja_form():
    dojos = Dojo.show_all_dojos()
    return render_template('new_ninja.html', dojos = dojos)

@app.route('/create/ninja', methods=['POST'])
def create_ninja():

    data = {
        'first_name': request.form['fname'],
        'last_name': request.form['lname'],
        'updated_at': 'NOW()',
        'created_at': 'NOW()',
        'dojo_id': request.form['dojo_id']

    }
    Ninja.create_ninja(data)

    return redirect (f"/dojos/{data['dojo_id']}")