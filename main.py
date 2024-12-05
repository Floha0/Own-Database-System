# CREATE, INSERT, DELETE, SELECT, UPDATE, COUNT, JOIN

# 58 times '#'

def print_table(table, table_name):
    print("Table: " + table_name)
    columns = table["columns"]
    rows = table["rows"]
    
    joined_columns = []

    for i in range(len(columns)):
        new_list = []
        new_list.append(columns[i])
        for row in rows:
            new_list.append(row[i])
        
        joined_columns.append(new_list)



    column_lengths = []
    for i in joined_columns:
        longest = len(max(i, key=len))
        column_lengths.append(longest)

    print("+", end='')
    for length in column_lengths:
        print("-"*(length+2)+"+",end='')
    print('')

    print("| ",end='')
    for i in range(len(columns)):
        gap = column_lengths[i] - len(columns[i])
        print(columns[i] + " "*gap + " | ",end='')
    print('')


    print("+", end='')
    for length in column_lengths:
        print("-"*(length+2)+"+",end='')
    print('')

    for i in range(len(rows)):
        print("|",end='')
        index = 0
        for j in range(len(rows[i])):
            gap = column_lengths[index] - len(rows[i][j])
            print(" "+rows[i][j] + " "*gap + " |",end='')
            index += 1
        print('')

    
    # index = 0
    # for i in range(len(joined_columns)):
    #     print("| ", end='')
    #     for j in range(len(joined_columns[i])):
    #         gap = column_lengths[index] - len(joined_columns[i][j])
    #         print(joined_columns[i][j] + " "*gap + " | ",end='')
    #         index = (index + 1) % len(column_lengths)
    #         print("{:{align}}| ".format(joined_columns[j][i], align=gap), end='')
            
    #     print('')

    print('+',end='')
    for length in column_lengths:
        print("-"*(length+2)+"+",end='')
    
    print('')

def printasd(asd):
    print(asd)

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
        print('#'*22+" CREATE "+'#'*25)
        print("Table '"+ table_name +"' created with columns: "+ str(columns))
        print('#'*55)
        
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
        print('#'*22+" INSERT "+'#'*25)
        tmp_text = ""
        tmp_text += "("
        for i in range(len(values)):
            if i != 0:
                tmp_text += " "
            tmp_text += "'"
            tmp_text += str(values[i])
            tmp_text += "'"
            if i < len(values)-1:
                tmp_text += ","
        tmp_text += ")"
        print("Inserted into '"+ table_name +"': " + tmp_text)
        print("")


        print_table(table,table_name)

        print('#'*55)

    def select(self, table_name, _columns, conditions):
        if table_name not in self.tables:
            print("Specified Table does not exist")
            return
        
        table = self.tables[table_name]
        columns = table["columns"]
        rows = table["rows"]

        rows_to_select = []
        condition_indexes = []

        for i in conditions:
            index = -1
            for column in columns:
                index += 1
                if column == i:
                    condition_indexes.append(index)
                    index = -1
                    break

        for row in rows:
            can_select = True
            for i, key in enumerate(conditions):  # Iterate over the keys
                # Compare the value at the index in the row with the condition value
                if row[condition_indexes[i]] != conditions[key]:
                    can_select = False
                    break
            if can_select:
                rows_to_select.append(row)

        for row in rows_to_select:
            print("Selected: ", row)

    def update(self, table_name, updates, conditions):
        if table_name not in self.tables:
            print("Specified Table does not exist")
            return
        
        table = self.tables[table_name]
        columns = table["columns"]
        rows = table["rows"]

        rows_to_update = []
        condition_indexes = []
        
        for i in conditions:
            index = -1
            for column in columns:
                index += 1
                if column == i:
                    condition_indexes.append(index)
                    index = -1
                    break

        for row in rows:
            can_update = True
            for i, key in enumerate(conditions):  # Iterate over the keys of the dictionary
                # Compare the value at the index in the row with the condition value
                if row[condition_indexes[i]] != conditions[key]:
                    can_update = False
                    break
            if can_update:
                rows_to_update.append(row)

        for row in rows_to_update:
            for i in updates:
                index = -1
                for column in columns:
                    index += 1
                    if column == i:
                        break
                row[index] = updates[i]

    def delete(self, table_name, conditions):
        if table_name not in self.tables:
            print("Specified Table does not exist")
            return
        
        table = self.tables[table_name]
        columns = table["columns"]
        rows = table["rows"]


        can_delete = True
        rows_to_delete = []

        index = -1
        for i in conditions:
            index = -1
            for column in columns:
                index += 1
                if column == i:
                    break

            found = False
            for row in rows:
                if row[index] == conditions[i]:
                    # rows.remove(row)
                    rows_to_delete.append(row)
                    found = True
                    break
            if not found:
                can_delete = False
                break

        if can_delete:
            for row in rows_to_delete:
                if row in rows:
                    rows.remove(row)
            print("Rows deleted successfully")
    
    # JOIN <table1>,<table2> ON <column>
    def join(self, table1_name, table2_name, _column):
        if table1_name not in self.tables or table2_name not in self.tables:
            print("Specified Table(s) does not exist")
            return

        # Find the tables, columns and rows    
        table1 = self.tables[table1_name]
        column1 = table1["columns"]
        rows1 = table1["rows"]

        table2 = self.tables[table2_name]
        column2 = table2["columns"]
        rows2 = table2["rows"]

        # Find the indexes of the columns
        column1_index = -1
        for col1 in column1:
            column1_index += 1
            if col1 == _column:
                break
        
        column2_index = -1
        for col2 in column2:
            column2_index += 1
            if col2 == _column:
                break

        # Create new table and insert the joined rows
        self.create_table("joined_table", column1 + column2)
        for row1 in rows1:
            for row2 in rows2:
                if row1[column1_index] == row2[column2_index]:
                    self.insert("joined_table", row1 + row2)
        
        print("Join tables "+table1_name+" and "+table2_name)
        print("Join result (" +str(len(self.tables["joined_table"]["rows"])) +" rows):")
        print("")
        print_table(self.tables["joined_table"], "Joined Table")
    def count(self, table_name, conditions):
        if table_name not in self.tables:
            print("Specified Table does not exist")
            return
        
        table = self.tables[table_name]
        columns = table["columns"]
        rows = table["rows"]

        rows_to_count = []
        condition_indexes = []

        for i in conditions:
            index = -1
            for column in columns:
                index += 1
                if column == i:
                    condition_indexes.append(index)
                    index = -1
                    break

        for row in rows:
            can_select = True
            for i, key in enumerate(conditions):
                if row[condition_indexes[i]] != conditions[key]:
                    can_select = False
                    break
            if can_select:
                rows_to_count.append(row)
        
        print("Count: ", len(rows_to_count))

sample_cmd = 'SELECT students id,name WHERE {"major": "CS"}'

parts = sample_cmd.strip().split(" ", 2)
cmd = parts[0].upper()      # SELECT, INSERT etc.
table_name, update_str = parts[1], parts[2]
# update_str is the rest of the text without cmd and table name
updates_part, where_part = update_str.split(" WHERE ")

# Parse updates and conditions
updates = updates_part.split(",")
conditions = eval(where_part)

print("Updates: ", updates)
print("conditions: ", conditions)



m = main()
m.create_table("students", ["id", "name", "age", "major"])
m.insert("students", ["1","John Doe","20","CS"])
m.insert("students", ["2","Jane Smith","22","EE"])
m.insert("students", ["3","Bob Wilson","21","CS"])

m.create_table("courses", ["course_id","name","major"])
m.insert("courses", ["101","Intro to Programming","CS"])
m.insert("courses", ["102","Circuit Design","EE"])
m.insert("courses", ["103","Data Structures","CS"])

# m.select("courses", ["course_id"], {"major": "CS", "course_id":"101"})
# m.update("courses", {"course_id": "51", "major": "IE"}, {"major": "CS"})
# m.delete("courses", {"major": "PE", "course_id":"103"})
# m.count("courses", {"major": "CS"})

m.join("students", "courses", "major")








input_text = ""
with open("i1.txt", "r", encoding="utf-8") as input_file:
    input_text = input_file.read()


cleaned_lines = input_text.splitlines()
cleaned_tokens = []

for i in cleaned_lines:
    cleaned_tokens.append(i.split())





# print_table = print_table(m.tables["courses"],"courses")
