-- Create 3 new users
INSERT INTO users(first_name, last_name, email, created_at, updated_at)
VALUES ("Charan", "Karthik", "charank15@outlook.com", NOW(), NOW()), ("Kaguya", "Shinomiya", "kaguya@shinomiyacorp.com", NOW(), NOW()), ("Zoro", "Roronoa", "zoro@bestswordsman.com", NOW(), NOW())

-- Retrieve all the users
SELECT * FROM users

-- Retrieve the first user using their email address
SELECT * FROM users WHERE email="charank15@outlook.com"

-- Retrieve the last user using their id
SELECT * FROM users WHERE id=3

-- Change the user with id=3 so their last name is Pancakes
UPDATE users SET last_name="Pancakes" WHERE id=3

-- Delete the user with id=2 from the database
DELETE FROM users WHERE id=2

-- Get all the users, sorted by their first name
SELECT * FROM users ORDER BY first_name

-- BONUS: Get all the users, sorted by their first name in descending order
SELECT * FROM users ORDER BY first_name DESC