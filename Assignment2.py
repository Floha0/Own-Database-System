# CREATE, INSERT, DELETE, SELECT, UPDATE, COUNT, JOIN

class main:
    def __init__(self):
        self.tables = {}

    def create_table(self, table_name, columns):
        if table_name in self.tables:
            print("Table is already exist")
            return
        
        # self.tables[table_name] = columns

        # Make a nested dictionary
        # The origin dictionary holds the tables
        # Key is table name, value is the table(as a new dictionary)
            # new dict's keys are columns and rows
            # columns holds a list of strings
            # rows hold a nested list.
        self.tables[table_name] = {"columns": columns, "rows": []}
        print("Table created successfully")
        
    def insert(self, table_name, values):
        if table_name not in self.tables:
            print("Specified Table does not exist")
            return
        
        table = self.tables[table_name]
        columns = table["columns"]
        
        # Check the length
        if len(values) != len(columns):
            print("length of values does not match with length of the columns")
            return
        
        # Insert the values
        table["rows"].append(values)
        print("Row inserted successfully")

    def select(self, table_name, _columns):
        if table_name not in self.tables:
            print("Specified Table does not exist")
            return
        
        table = self.tables[table_name]
        columns = table["columns"]
        rows = table["rows"]

        selected_values = []

        if _columns[0] == "*":
            for i in range(len(columns)):
                    selected_values.append(rows[i])
        else:
            for i in range(len(columns)):
                if columns[i] in _columns:
                    selected_values.append(rows[i])


        print("Selected Values: ", selected_values)


m = main()
m.create_table("students", ["id", "name", "age"])
m.insert("students", [1,"a",17])

m.create_table("courses", ["course_id","name","major"])
m.insert("courses", [101,"Intro to Programming","CS"])
m.insert("courses", [102,"Circuit Design","EE"])

m.select("courses", ["course_id"])

print(m.tables)







print("-"*100)

input_text = ""
with open("i1.txt", "r", encoding="utf-8") as input_file:
    input_text = input_file.read()


cleaned_lines = input_text.splitlines()
cleaned_tokens = []

for i in cleaned_lines:
    cleaned_tokens.append(i.split())