from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models.user import User

class Recipe:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.under_30 = data["under_30"]
        self.instructions = data["instructions"]
        self.date_made = data["date_made"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.poster = None
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipies JOIN users ON users.id = recipies.user_id"
        results = connectToMySQL("recipe_schema").query_db(query)
        # print(results)

        all_recipies = []
        for recipe in results:
            single_recipe = cls(recipe)

            user_data = {
                "id": recipe["users.id"],
                "first_name": recipe["first_name"],
                "last_name": recipe["last_name"],
                "email": recipe["email"],
                "password": recipe["password"],
                "updated_at": recipe["users.updated_at"],
                "created_at": recipe["users.created_at"]
            }
            
            single_recipe.poster = User(user_data)
            all_recipies.append(single_recipe)

        # print(recipies)

        return all_recipies
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipies(name, description, under_30, instructions, date_made, created_at, updated_at, user_id) VALUES(%(name)s, %(description)s,%(under_30)s,%(instructions)s,%(date_made)s,NOW(),NOW(),%(user_id)s)"

        return connectToMySQL("recipe_schema").query_db(query, data)

    @classmethod
    def get_one_recipe(cls, data):
        query = "SELECT * FROM recipies WHERE id=%(id)s"
        results = connectToMySQL("recipe_schema").query_db(query, data)
        
        one_recipe = cls(results[0])
        return one_recipe
    
    @classmethod
    def edit_recipe(cls, data):
        query = "UPDATE recipies SET name=%(name)s, description=%(description)s, under_30=%(under_30)s, instructions=%(instructions)s, date_made=%(date_made)s, updated_at=NOW() WHERE id=%(id)s"

        return connectToMySQL("recipe_schema").query_db(query, data)
    
    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipies WHERE id=%(id)s"

        return connectToMySQL("recipe_schema").query_db(query, data)

