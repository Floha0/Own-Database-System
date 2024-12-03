# CREATE, INSERT, DELETE, SELECT, UPDATE, COUNT, JOIN

class main:
    def __init__(self):
        self.tables = {}

    def create_table(self, table_name, columns):
        
        if table_name in self.tables:
            print("Table is exist")
            return
        
        