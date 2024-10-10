import sqlite3

# Connect to your database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Fetch the schema for the users table
cursor.execute("PRAGMA table_info(users);")
columns = cursor.fetchall()

# Print the columns
print("Current columns in the 'users' table:")
for column in columns:
    print(column)

conn.close()
