-- SELECT * FROM users
-- SELECT * FROM friendships

# Create 6 New Users
-- INSERT INTO users(first_name, last_name)
-- VALUES("John", "Doe"), ("Jane", "Doe"), ("Anakin", "Skywalker"), ("Luke", "Skywalker"), ("Master", "Yoda"), ("Boba", "Fett")

# Have user 1 be friends with user 2, 4, and 6
-- INSERT INTO friendships(user_id, friend_id)
-- VALUES(1,2), (1,4), (1,6)

# Have user 2 be friends with user 1, 3, and 5
-- INSERT INTO friendships(user_id, friend_id)
-- VALUES(2,1), (2,3), (2,5)

# Have user 3 be friends with user 2 and 5
-- INSERT INTO friendships(user_id, friend_id)
-- VALUES(3,2), (3,5)

# Have user 4 be friends with user 3
-- INSERT INTO friendships(user_id, friend_id)
-- VALUES(3,4)

# Have user 5 be friends with user 1 and 6
-- INSERT INTO friendships(user_id, friend_id)
-- VALUES(5,1), (5,6)

# Have user 6 be friends with user 2 and 3
-- INSERT INTO friendships(user_id, friend_id)
-- VALUES(6,2), (6,3)

# Display the relationships created as shown in the table in the assignment description
-- SELECT users.first_name, users.last_name, users2.first_name as friend_first_name, users2.last_name as friend_last_name FROM users
-- JOIN friendships ON users.id=friendships.user_id
-- LEFT JOIN users as users2 ON users2.id = friendships.friend_id

# Return all users who are friends with the first user, make sure their names are displayed in results
-- SELECT users2.first_name, users2.last_name, users.first_name FROM users
-- JOIN friendships on users.id = friendships.user_id
-- LEFT JOIN users as users2 ON users2.id = friendships.friend_id WHERE users.id=1

# Return the count of all friendships
-- SELECT COUNT(*) from friendships

# Find out who has the most friends and return the count of their friends
-- SELECT users.first_name, users.last_name, count(user_id) FROM friendships
-- JOIN users ON users.id = friendships.user_id
-- GROUP BY user_id
-- ORDER BY count(user_id) DESC
-- LIMIT 1

# Return the friends of the third user in alphabetical order
-- SELECT users2.first_name, users2.last_name, users.first_name as "friends_with" FROM users
-- JOIN friendships ON users.id = friendships.user_id
-- LEFT JOIN users as users2 ON users2.id = friendships.friend_id
-- WHERE users.id=3 ORDER BY first_name