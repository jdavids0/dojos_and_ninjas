from flask_app.config.mysqlconnection import connectToMySQL

# from flask_app.models.dojo import Dojo

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo = None

    @classmethod
    def create_ninja (cls,data):
        # if not working, make sure order of variables matches order of table columns
        query = "INSERT INTO ninjas (first_name, last_name, created_at, updated_at, dojo_id) VALUES ( %(first_name)s, %(last_name)s, NOW(), NOW(), %(dojo_id)s )"

        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    # @classmethod
    # def show_all_ninjas():
    #     pass
        # query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s;"

        #     results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)        
        #     ninjas = []
        #     for x in results:
        #         ninjas.append(cls(x))
        #     return ninjas