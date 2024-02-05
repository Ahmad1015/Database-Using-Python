from Print_Write import Print_Write
class SQLParser:
    def __init__(self, db):
        self.db = db

    def handle(self, command):
        command = command.strip()
        command = command.strip()
        if command.endswith(';'):
            command = command[:-1]
        tokens = self.split_into_parts(command)
        tree = self.parse(tokens)
        return self.solver(tree)


    def split_into_parts(self, command):
        return command.split()

    def parse(self, tokens): # Simple String parsing to check what is there in String
        tree = {"command": tokens[0]}
        if tree["command"] == "CREATE":
            tree["table"] = tokens[2]
            columns_string = ' '.join(tokens[3:]).replace('(', '').replace(')', '') # Removing brackets
            tree["columns"] = [column.strip() for column in columns_string.split(',') if column.strip()] # Separating Columns using List comprehension
        elif tree["command"] == "INSERT":
            tree["table"] = tokens[2]
            values_string = ' '.join(tokens[4:]).rstrip(',')
            tree["values"] = [value.strip() for value in values_string.replace('(', '').replace(')', '').split(',') if value]
        elif tree["command"] == "SELECT":
            if "*" in tokens[1]:
                tree["columns"] = "*"
            else:
                tree["columns"] = tokens[1].split(",")
            tree["table"] = tokens[3]
            if "WHERE" in tokens:
                where_index = tokens.index("WHERE")
                tree["where"] = ' '.join(tokens[where_index + 1:])
        elif tree["command"] == "DELETE":
            tree["table"] = tokens[2]
            if "WHERE" in tokens:
                where_index = tokens.index("WHERE")
                tree["where"] = ' '.join(tokens[where_index + 1:])
        return tree

    def solver(self, tree):
        if tree["command"] == "CREATE":
            self.db.create_table(tree["table"], tree["columns"])
        elif tree["command"] == "INSERT":
            result = self.db.insert_into(tree["table"], tree["values"])
            pw = Print_Write(result, self.db.tables[tree['table']]['columns'])
            result = pw.write_tsv(tree['table'])
            return result

        elif tree["command"] == "SELECT":
            result = self.db.select_from(tree["table"], tree["columns"], tree.get("where"))


            pw = Print_Write(result,self.db.tables[tree['table']]['columns'])
            result = pw.write_tsv(tree['table'])

            return result

        elif tree["command"] == "DELETE":
            result = self.db.delete_from(tree["table"], tree.get("where"))
            pw = Print_Write(result, self.db.tables[tree['table']]['columns'])
            result = pw.write_tsv(tree['table'])

            return result