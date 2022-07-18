# Create 5 Different Users
-- INSERT INTO users(first_name, last_name, created_at, updated_at)
-- VALUES("Jane", "Amsden", NOW(), NOW()), ("Emily", "Dixon", NOW(), NOW()), ("Theodore", "Dostoevsky", NOW(), NOW()), ("William", "Shapiro", NOW(), NOW()), ("Lao", "Xiu", NOW(), NOW());

-- SELECT * FROM users
-- SELECT * FROM books
-- SELECT * FROM favorites

# Create 5 Books
-- INSERT INTO books(title)
-- VALUES("C Sharp"), ("Java"), ("Python"), ("PHP"), ("Ruby")

# Change the ame of the C Sharp book to "C#"
-- UPDATE books SET title="C#" WHERE id=1

# Change the name of rht 4th user to Bill
-- UPDATE users SET first_name="Bill" WHERE id=4

-- # Have the first user favorite the first 2 books
-- INSERT INTO favorites(user_id, book_id)
-- VALUES (1,1), (1,2)

# Have the second user favorite the first 3 books
-- INSERT INTO favorites(user_id, book_id)
-- VALUES (2,1), (2,2), (2,3)

# Have the third user favorite the first 4 books
-- INSERT INTO favorites(user_id, book_id)
-- VALUES (3,1), (3,2), (3,3), (3,4)

# Have the fourth user favorite all the books
-- INSERT INTO favorites(user_id, book_id)
-- VALUES (4,1), (4,2), (4,3), (4,4), (4,5)

# Retrieve all the users who favorited the 3rd book
-- SELECT * FROM users
-- JOIN favorites on users.id=favorites.user_id
-- JOIN books on favorites.book_id=books.id
-- WHERE books.id=3

# Remove the first user of the 3rd book's favorites
-- DELETE FROM favorites WHERE user_id=2 AND book_id=3

# Have the 5th user favorite the 2nd book
-- INSERT INTO favorites(user_id, book_id)
-- VALUES (5,2)

# Find all the books that the 3rd user favorited
-- SELECT title from books
-- JOIN favorites on favorites.book_id = books.id
-- WHERE favorites.user_id=3

# Find all the users that favorited the 5th book
SELECT * from users
JOIN favorites on users.id = favorites.user_id
WHERE favorites.book_id=5
