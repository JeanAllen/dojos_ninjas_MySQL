# import the function that will return an instance of a connection
from dojos_ninjas_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from dojos_ninjas_app.models import ninja


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_ninjas').query_db(query)
        # Create an empty list to append our instances of friends
        all_dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            all_dojos.append(cls(dojo))
        return all_dojos

    @classmethod
    def create_new(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(dojo_name)s, NOW(), NOW());"
        dojo_id = connectToMySQL(
            'dojos_ninjas').query_db(query, data)
        return dojo_id

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id=ninjas.dojo_id WHERE dojos.id=%(id)s;"
        results = connectToMySQL('dojos_ninjas').query_db(query, data)
        dojo = cls(results[0])
        for row in results:
            row_data = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append(ninja.Ninja(row_data))
        return dojo
