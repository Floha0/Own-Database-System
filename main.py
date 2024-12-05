# CREATE, INSERT, DELETE, SELECT, UPDATE, COUNT, JOIN
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('input_file', type=str)
parser.add_argument('output_file', type=str)

args = parser.parse_args()

input_filename = args.input_file
output_filename = args.output_file



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
        print(columns[i] + " "*gap,end='')
        if i == len(columns)-1:
            print(" |",end='')
        else:
            print(" | ",end='')
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

    print('+',end='')
    for length in column_lengths:
        print("-"*(length+2)+"+",end='')
    
    print('')

class main:
    def __init__(self):
        self.tables = {}

    def create_table(self, table_name, columns, can_print=True):
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
        if can_print:
            print('#'*22+" CREATE "+'#'*25)
            print("Table '"+ table_name +"' created with columns: "+ str(columns))
            print('#'*55)
        
    def insert(self, table_name, values, can_print=True):
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

        if can_print:
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


        print('#'*22+" SELECT "+'#'*25)
        print("Condition: " + str(conditions))        

        print("Select result from '"+table_name+"': [",end='')
        for j in range(len(rows_to_select)):
            tmp_text = ""
            tmp_text += "("
            for i in range(len(rows_to_select[j])):
                if i != 0:
                    tmp_text += " "
                tmp_text += "'"
                tmp_text += str(rows_to_select[j][i])
                tmp_text += "'"
                if i < len(rows_to_select[j])-1:
                    tmp_text += ","
            tmp_text += ")"
            print(tmp_text, end='')
            if j < len(rows_to_select)-1:
                print(", ", end='')
        print("]")

        print('#'*55)

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

        print('#'*22+" UPDATE "+'#'*25)
        print("Updated '"+table_name+"' with "+str(updates)+" where "+str(conditions))
        print(str(len(rows_to_update))+" rows updated.")
        print("")
        print_table(table,table_name)
        print('#'*55)

    def delete(self, table_name, conditions):
        if table_name not in self.tables:
            print("Specified Table does not exist")
            return
        
        table = self.tables[table_name]
        columns = table["columns"]
        rows = table["rows"]


        rows_to_delete = []
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
            can_delete = True
            for i, key in enumerate(conditions):  # Iterate over the keys
                # Compare the value at the index in the row with the condition value
                if row[condition_indexes[i]] != conditions[key]:
                    can_delete = False
                    break
            if can_delete:
                rows_to_delete.append(row)

        for row in rows_to_delete:
            rows.remove(row)
            

        print('#'*22+" DELETE "+'#'*25)
        print("Deleted from '"+table_name+"' where "+str(conditions))
        print(str(len(rows_to_delete))+" rows deleted.")
        print("")
        print_table(table,table_name)
        print('#'*55)


        
    
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
        self.create_table("joined_table", column1 + column2, False)
        for row1 in rows1:
            for row2 in rows2:
                if row1[column1_index] == row2[column2_index]:
                    self.insert("joined_table", row1 + row2, False)
        
        print('#'*23+" JOIN "+'#'*26)
        print("Join tables "+table1_name+" and "+table2_name)
        print("Join result (" +str(len(self.tables["joined_table"]["rows"])) +" rows):")
        print("")
        print_table(self.tables["joined_table"], "Joined Table")
        print('#'*55)


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
        
        print('#'*23+" COUNT "+'#'*24)
        print("Count: ", len(rows_to_count))
        print("Total number of entries in '"+table_name+"' is "+str(len(rows_to_count)))
        print('#'*55)



m = main()

input_text = open(input_filename, "r").read()
cleaned_lines = input_text.splitlines()
cleaned_tokens = []

for i in cleaned_lines:
    cleaned_tokens.append(i.split())

tmp_index = 0
for i in cleaned_tokens:
    if len(i) > 0:
        if tmp_index != 0:
            print("")

        if i[0] == "CREATE_TABLE":
            # 0: CREATE_TABLE, 1: table_name, 2: columns
            splitted_columns = i[2].split(",")
            m.create_table(i[1],splitted_columns)
        if i[0] == "INSERT":
            # 0: INSERT, 1: table_name, 2: values
            table_name = i[1]
            values = " ".join(i[2:])
            splitted_values = values.split(",")
            m.insert(i[1],splitted_values)
        if i[0] == "SELECT":
            # 0: SELECT, 1: table_name, 2: columns, 3: WHERE, 4: conditions
            table_name = i[1]
            columns = i[2].split(",")
            tmp_tokens = i[4:]
            conditions = eval(" ".join(tmp_tokens))
            conditions = {str(k): str(v) for k, v in conditions.items()} # Convert keys and values to string
            m.select(table_name, columns, conditions)
        if i[0] == "UPDATE":
            # 0: UPDATE, 1: table_name, 2: updates, 3: WHERE, 4: conditions
            table_name = i[1]
            tmp_tokens = " ".join(i[2:]).split(" WHERE ")
            updates = eval(tmp_tokens[0])
            updates = {str(k): str(v) for k, v in updates.items()} # Convert keys and values to string
            
            conditions = eval(tmp_tokens[1])
            conditions = {str(k): str(v) for k, v in conditions.items()} # Convert keys and values to string
            m.update(table_name, updates, conditions)
        if i[0] == "DELETE":
            # 0: DELETE, 1: table_name, 2: WHERE, 3: conditions
            table_name = i[1]
            conditions = eval(" ".join(i[3:]))
            conditions = {str(k): str(v) for k, v in conditions.items()} # Convert keys and values to string
            m.delete(table_name, conditions)
        if i[0] == "JOIN":
            # 0: JOIN, 1: table_names, 2: ON, 3: column
            table1_name, table2_name = i[1].split(",")
            column = i[3]
            m.join(table1_name, table2_name, column)
        if i[0] == "COUNT":
            # 0: COUNT, 1: table_name, 2: WHERE, 3: conditions
            table_name = i[1]
            conditions = eval(" ".join(i[3:]))
            conditions = {str(k): str(v) for k, v in conditions.items()}
            m.count(table_name, conditions)
        tmp_index += 1