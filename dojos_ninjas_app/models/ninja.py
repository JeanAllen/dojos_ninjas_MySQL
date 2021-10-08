from dojos_ninjas_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        #self.dojo = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas"
        results = connectToMySQL('dojos_ninjas').query_db(query)
        all_ninjas = []
        for ninja in results:
            all_ninjas.append(cls(ninja))
        return all_ninjas

    @classmethod
    def add_new(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id,created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s,%(dojo_id)s, NOW(), NOW());"
        ninja_id = connectToMySQL(
            'dojos_ninjas').query_db(query, data)
        return ninja_id
