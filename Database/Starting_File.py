from Database import Database
from SqlParer import SQLParser


class Starting_File:
    def __init__(self):
        self.data = None
        self.db = Database()
        self.parser = SQLParser(self.db)

    def get_input(self,SQL):
        return self.parser.handle(SQL)

