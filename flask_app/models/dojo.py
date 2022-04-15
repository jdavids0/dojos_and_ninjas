from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def show_all_dojos(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)

        dojos = []
        for x in results:
            dojos.append(cls(x))
        return dojos

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos ( name, created_at, updated_at ) VALUES ( %(name)s, NOW(), NOW() )"
        
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

        return result

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos ( name, created_at, updated_at ) VALUES ( %(name)s, NOW(), NOW() )";

        return connectToMySQL('ninjas').query_db(query, data)

    @classmethod
    def get_dojos_with_ninjas(cls, data):
        query = "SELECT * from dojos LEFT JOIN ninjas on ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s";

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

        dojo = []
        for row in results:

            ninja_data = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }

            dojo.append(ninja_data)

        return dojo

    @classmethod
    def get_dojo_name(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"

        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return result[0]