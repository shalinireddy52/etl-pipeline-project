import sqlite3
import pandas as pd

# Connect to SQLite database (or create it)
conn = sqlite3.connect("data/data.db")
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, userId INTEGER, title TEXT, body TEXT)''')

# Load transformed data
df = pd.read_csv("data/transformed_data.csv")

# Insert data into the database
for _, row in df.iterrows():
    cursor.execute("INSERT INTO posts (id, userId, title, body) VALUES (?, ?, ?, ?)",
                   (row['id'], row['userId'], row['title'], row['body']))

# Commit and close the connection
conn.commit()
conn.close()

print("Data loaded into SQLite database")
