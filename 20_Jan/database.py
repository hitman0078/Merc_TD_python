import sqlite3

class DatabaseManager:
    def __init__(self, db_name="mydatabase.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
        """)
        self.conn.commit()

    # CREATE
    def insert_user(self, name, age):
        self.cursor.execute(
            "INSERT INTO users (name, age) VALUES (?, ?)",
            (name, age)
        )
        self.conn.commit()
        print("✅ User added successfully.")

    # READ
    def fetch_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    # UPDATE
    def update_user(self, user_id, name, age):
        self.cursor.execute(
            "UPDATE users SET name = ?, age = ? WHERE id = ?",
            (name, age, user_id)
        )
        self.conn.commit()
        return self.cursor.rowcount

    # DELETE
    def delete_user(self, user_id):
        self.cursor.execute(
            "DELETE FROM users WHERE id = ?",
            (user_id,)
        )
        self.conn.commit()
        return self.cursor.rowcount

    def close(self):
        self.conn.close()