
import sqlite3
import matplotlib
matplotlib.use("TkAgg")


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('footballscaut.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS footballscaut (id integer primary key, name text, age text, height text,
            position text, information text, citizenship text, club text, price text, pace text, shooting text, passing text, dribbling text, defending text, physicality text)''')
        self.conn.commit()

    def insert_data(self, name, age, height, position, information, citizenship, club, price,pace, shooting, passing, dribbling, defending, physicality):
        self.c.execute('''INSERT INTO footballscaut (name, age, height, position, 
        information, citizenship, club, price, pace, shooting, passing, dribbling, defending, physicality) VALUES (?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?,?,?)''',
                       (name, age, height, position, information, citizenship, club, price, pace, shooting, passing, dribbling, defending, physicality))
        self.conn.commit()