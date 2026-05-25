import mysql.connector

# Connect to MySQL Server
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin"
)

cursor = db.cursor()

# Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS habit_tracker")

# Use Database
cursor.execute("USE habit_tracker")

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS habits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    status BOOLEAN DEFAULT 0,
    streak INT DEFAULT 0
)
""")

print("Database and table created successfully!")

db.close()