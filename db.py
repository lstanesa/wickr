import sqlite3 as sqlite
import os

class Database:
    def __init__(self, dbpath, autoconnect=False):
        self.dbh = None
        self.cursor = None
        self.dbpath = dbpath

        if autoconnect:
            if os.path.isfile(self.dbpath):
                self.connect()
            else:
                self.create()

    def create(self):
        self.connect()
        query = open('schema.sql', 'r').read()
        self.cursor.executescript(query)
        self.dbh.commit()
        self.cursor.close()
        self.dbh.close()

    def clean(self):
        os.remove(self.dbpath)
        self.create()

    def connect(self):
        self.dbh = sqlite.connect(self.dbpath)
        self.cursor = self.dbh.cursor()

    def query(self, qry, binds=[]):
        return self.cursor.execute(qry, binds)

    def commit(self):
        self.dbh.commit()

    def close(self, docommit=False):
        self.commit()
        self.cursor.close()
        self.dbh.close()

    def last_row_id(self):
        return self.cursor.lastrowid


