import sqlite3

# Connect to your database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create a new users table with the correct columns
cursor.execute('''
CREATE TABLE new_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    first_name TEXT,
    last_name TEXT,
    email TEXT
)
''')

# Copy data from the old users table to the new_users table
cursor.execute('''
INSERT INTO new_users (id, username, password)
SELECT id, username, password FROM users
''')

# Drop the old users table
cursor.execute('DROP TABLE users')

# Rename the new_users table to users
cursor.execute('ALTER TABLE new_users RENAME TO users')

conn.commit()
conn.close()
