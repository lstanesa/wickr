from flask import g
import datetime

class Article:
    def __init__(self, name=None, content=None, created=None):
        #if name:
        #    name = name.replace(' ', '_')

        self.id = None
        self.name = name
        self.content = content
        self.created = created

        if self.created:
            stamp = self.created
            self.created = datetime.datetime.fromtimestamp(stamp).strfttime('%d/%m/%y')
    
    def insert(self):
        return g.db.query('INSERT INTO article (name, content, created) VALUES (?, ?, ?)', [self.name, self.content, self.created ])

    def fetch(self):
        row = g.db.query('SELECT `id`,`content`,`created` FROM article WHERE name=?', [self.name]).fetchone()
        if row:
            self.id = row[0]
            self.content = row[1]
            self.created = row[2]
            stamp = self.created
            self.created = datetime.datetime.fromtimestamp(stamp).strftime('%d/%m/%y')
