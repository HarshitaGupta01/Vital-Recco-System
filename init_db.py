import sqlite3

# Connect to SQLite (or create it)
conn = sqlite3.connect('database.db')

# Create a cursor
cur = conn.cursor()
# Create the table
cur.execute('''CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    appointment_date TEXT NOT NULL,
    appointment_time TEXT NOT NULL,
    doctor TEXT NOT NULL
)''')


# Create the inquiries table for storing contact form submissions
cur.execute('''CREATE TABLE IF NOT EXISTS inquiries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    subject TEXT NOT NULL,
    message TEXT NOT NULL
)''')


# Commit and close
conn.commit()
conn.close()

print("Database and table created successfully!")
