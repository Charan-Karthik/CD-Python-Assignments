# SELECT * FROM dojos
-- SELECT * FROM ninjas

# Create 3 new dojos
-- INSERT INTO dojos(name)
-- VALUES("Burbank"), ("Bellevue"), ("San Jose")

# Delete the 3 dojos you just created
-- SET SQL_SAFE_UPDATES = 0;
-- DELETE FROM dojos

# Create 3 more dojos
-- INSERT INTO dojos(name)
-- VALUES("Silicon Valley"), ("Chicago"), ("ONLINE")

# Create 3 ninjas that belong to the first dojo
-- INSERT INTO ninjas(first_name, last_name, age, dojos_id)
-- VALUES ("Charan", "Karthik", 21, 4), ("Naruto","Uzumaki",17,4), ("Sasuke","Uchiha",17,4)

# Create 3 ninjas that belong to the second dojo
-- INSERT INTO ninjas(first_name, last_name, age, dojos_id)
-- VALUES ("Mike", "Mazur", 25, 5), ("Tony","Stark",35,5), ("Steve","Rodgers",99,5)

# Create 3 ninjas that belong to the third dojo
-- INSERT INTO ninjas(first_name, last_name, age, dojos_id)
-- VALUES ("Jon","Apple",39,6), ("Jane","Doe",27,6), ("I am", "Groot", 14, 6)

# Retrieve all the ninjas from the first dojo
-- SELECT * FROM ninjas WHERE dojos_id = 4

# Retrieve all the ninjas from the last dojo
-- SELECT * FROM ninjas WHERE dojos_id = 6

# Retrieve the last ninja's dojo
-- SELECT dojos_id from ninjas WHERE id=9