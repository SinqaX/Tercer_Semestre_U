import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS materials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                category TEXT,
                quantity INTEGER,
                last_entry TEXT,
                last_exit TEXT,
                FOREIGN KEY(category) REFERENCES categories(name)
            )
        ''')
        self.conn.commit()

    def get_categories(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT name FROM categories')
        return [row[0] for row in cursor.fetchall()]

    def add_category(self, category_name):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO categories (name) VALUES (?)', (category_name,))
        self.conn.commit()

    def get_materials_by_category(self, category):
        cursor = self.conn.cursor()
        cursor.execute('SELECT name FROM materials WHERE category = ?', (category,))
        return [{'name': row[0]} for row in cursor.fetchall()]

    def add_material(self, material_name, category):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO materials (name, category, quantity, last_entry, last_exit)
            VALUES (?, ?, 0, '', '')
        ''', (material_name, category))
        self.conn.commit()

    def get_material(self, material_name):
        cursor = self.conn.cursor()
        cursor.execute('SELECT name, quantity, last_entry, last_exit FROM materials WHERE name = ?', (material_name,))
        row = cursor.fetchone()
        return {'name': row[0], 'quantity': row[1], 'last_entry': row[2], 'last_exit': row[3]}

    def update_material_quantity(self, material_name, quantity, action):
        cursor = self.conn.cursor()
        if action == 'entry':
            cursor.execute('''
                UPDATE materials
                SET quantity = quantity + ?, last_entry = ?
                WHERE name = ?
            ''', (quantity, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), material_name))
        elif action == 'exit':
            cursor.execute('''
                UPDATE materials
                SET quantity = quantity - ?, last_exit = ?
                WHERE name = ?
            ''', (quantity, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), material_name))
        self.conn.commit()
