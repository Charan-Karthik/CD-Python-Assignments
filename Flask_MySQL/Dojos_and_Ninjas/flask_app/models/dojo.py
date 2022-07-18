from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL("dojos_and_ninjas").query_db(query)

        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos(name, created_at, updated_at) VALUES(%(name)s, NOW(), NOW())"
        return connectToMySQL("dojos_and_ninjas").query_db(query, data)

    @classmethod
    def ninjas_in_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojos_id WHERE dojos.id=%(id)s"
        results = connectToMySQL("dojos_and_ninjas").query_db(query, data)

        # print(results)

        single_dojo = cls(results[0])
        
        if "ninjas.id" in results[0]:
            for ninja in results:
                ninja_data = {
                    "id": ninja["ninjas.id"],
                    "first_name": ninja["first_name"],
                    "last_name": ninja["last_name"],
                    "age": ninja["age"],
                    "dojos_id": ninja["dojos_id"],
                    "created_at": ninja["created_at"],
                    "updated_at": ninja["updated_at"],
                }

                single_dojo.ninjas.append(Ninja(ninja_data))
        
        return single_dojo