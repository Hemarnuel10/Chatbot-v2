import sqlite3

connection = sqlite3.connect("emma_ai.db")

print("Database connected successfully!")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_message TEXT,
    ai_response TEXT,
    provider TEXT,
    model TEXT,
    timestamp TEXT
)
""")

cursor.execute("""
INSERT INTO conversations (
    user_message,
    ai_response,
    provider,
    model,
    timestamp
)
VALUES (?, ?, ?, ?, ?)
""", (
    "Hello",
    "Hello! How can I help you?",
    "Gemini",
    "gemini-2.5-flash",
    "2026-07-25 20:00"
))

connection.commit()

cursor.execute("SELECT * FROM conversations")

rows = cursor.fetchall()

print(rows)

connection.close()