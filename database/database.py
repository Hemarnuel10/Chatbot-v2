import sqlite3

connection = sqlite3.connect("emma_ai.db")

print("Database connected successfully!")

connection.close()