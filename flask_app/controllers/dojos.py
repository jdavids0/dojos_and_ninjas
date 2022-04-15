from flask_app import app

from flask import render_template, request, redirect

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    return redirect ('/dojos')

@app.route('/dojos')
def show_all():
    dojos = Dojo.show_all_dojos()
    return render_template ('dojos.html', dojos = dojos)

@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    
    data = {
            'name': request.form['dojo_name'],
            'updated_at': 'NOW()',
            'updated_at': 'NOW()',
        }
    Dojo.create_dojo(data)

    return redirect ('/dojos')

@app.route('/dojos/<int:id>')
def show_ninjas(id):
    data = {
        'id': id
    }
    ninjas = Dojo.get_dojos_with_ninjas(data)
    dojo = Dojo.get_dojo_name(data)
    return render_template('show_dojo.html', ninjas = ninjas, dojo = dojo)
