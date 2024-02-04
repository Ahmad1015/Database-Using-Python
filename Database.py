from SqlParer import SQLParser


class Database:
    def __init__(self):
        self.tables = {}

    def create_table(self, table_name, column_names):
        self.tables[table_name] = {"columns": column_names, "rows": []}

    def insert_into(self, table_name, values):
        if table_name in self.tables:
            values = [value.strip("'") for value in values]
            row = {column: value for column, value in zip(self.tables[table_name]["columns"], values)}
            self.tables[table_name]["rows"].append(row)
        else:
            raise ValueError(f"Table '{table_name}' does not exist.")

    def select_from(self, table_name, columns, where=None):
        if table_name in self.tables:
            selected_rows = []
            for row in self.tables[table_name]["rows"]:
                if where is None or self.solve_where(where,row):
                    if columns == "*":
                        selected_rows.append(list(row.values()))
                    else:
                        selected_rows.append([row[column] for column in columns])
            return selected_rows
        else:
            raise ValueError(f"Table '{table_name}' does not exist.")

    def solve_where(self, where,row):
        operators = ['>=', '<=', '>', '<', '=']
        for op in operators:
            if op in where:
                name, condition = where.split(op)
                break
        name = name.strip()
        condition = condition.strip()
        for key in row:
            if name in key:
                datatype = key.split(' ')[1]
                value = row[key]
                if datatype == 'INT':
                    value = int(value)
                    condition = int(condition)
                elif datatype == 'FLOAT':
                    value = float(value)
                    condition = float(condition)
                # If datatype is STRING, no need to typecast
                if op == '>=':
                    return value >= condition
                elif op == '<=':
                    return value <= condition
                elif op == '>':
                    return value > condition
                elif op == '<':
                    return value < condition
                elif op == '=':
                    return value == condition
        return "Name not found in the dictionary"

    def delete_from(self, table_name, where=None):
        if table_name in self.tables:
            self.tables[table_name]["rows"] = [row for row in self.tables[table_name]["rows"] if
                                               not (where is None or self.solve_where(where, row))]
        else:
            raise ValueError(f"Table '{table_name}' does not exist.")


db = Database()
parser = SQLParser(db)
parser.handle("CREATE TABLE customers (id INT, name STRING, email STRING)")
parser.handle("INSERT INTO customers VALUES (1, 'John Doe', 'johndoe@example.com')")
parser.handle("INSERT INTO customers VALUES (2, 'Jane Doe', 'janedoe@example.com')")

parser.handle("SELECT * FROM customers")
