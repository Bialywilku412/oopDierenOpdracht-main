# Dier.py
# Anjo Eijeriks
# 2023/11/30 V3

class Dier:
    def __init__(self, dierid, soort, naam):
        # Use double underscores to make attributes private
        self.__dierid = dierid
        self.__soort = soort
        self.__naam = naam

        self.conn = None
        self.cursor = None

    def open_database(self):
        import sqlite3
        self.conn = sqlite3.connect('dierentuin.db')
        self.cursor = self.conn.cursor()

    def sluit_database(self):
        self.conn.commit()
        self.conn.close()

    def create_dier(self, dierid, soort, naam):
        # Avoid unnecessary assignments to instance variables
        self.open_database()
        insert_query = """INSERT INTO dieren(soort, naam) VALUES(?, ?)"""
        self.cursor.execute(insert_query, (soort, naam))
        self.sluit_database()

    def read_dieren(self):
        # Remove unnecessary parameters from the method signature
        self.open_database()
        select_query = """SELECT * FROM dieren"""
        self.cursor.execute(select_query)
        dieren = self.cursor.fetchall()
        self.sluit_database()
        return dieren

    def update_dier(self, dierid, soort, naam):
        update_query = """UPDATE dieren SET soort = ?, naam = ? WHERE dierid = ?"""
        self.cursor.execute(update_query, (soort, naam, dierid))
        # Add necessary code here

    def delete_dier(self, dierid):
        self.open_database()
        delete_query = """DELETE FROM dieren WHERE dierid = ?"""
        self.cursor.execute(delete_query, (dierid,))
        # Add necessary code here
        self.sluit_database()

    def search_dier(self, dierid):
        self.open_database()
        select_query = """SELECT * FROM dieren WHERE dierid = ?"""
        self.cursor.execute(select_query, (dierid,))
        dieren = self.cursor.fetchall()
        self.sluit_database()
        return dieren

    
    # SETTERS EN GETTERS ZIJN NIET NODIG --------------------------------------