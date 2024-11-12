import sqlite3
import os

# Función para crear una conexión a la base de datos
def create_connection():
    db_path = os.path.join(os.path.dirname(__file__), '../db/database.db')
    conn = sqlite3.connect(db_path)
    return conn

# Función para crear la tabla de productos
def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            quantity INTEGER,
            price REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()