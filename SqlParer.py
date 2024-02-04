
class SQLParser:
    def __init__(self, db):
        self.db = db

    def handle(self, command):
        tokens = self.tokenize(command)
        tree = self.parse(tokens)
        self.interpret(tree)

    def tokenize(self, command):
        return command.split()

    def parse(self, tokens):
        tree = {"command": tokens[0]}
        if tree["command"] == "CREATE":
            tree["table"] = tokens[2]
            columns_string = ' '.join(tokens[3:]).replace('(', '').replace(')', '')
            tree["columns"] = [column.strip() for column in columns_string.split(',') if column.strip()]
        elif tree["command"] == "INSERT":
            tree["table"] = tokens[2]
            # remove the parentheses and split the values string into a list
            values_string = ' '.join(tokens[4:]).rstrip(',')
            tree["values"] = [value.strip() for value in values_string.replace('(', '').replace(')', '').split(',') if
                              value]
        elif tree["command"] == "SELECT":
            if tokens[1] == "*":
                tree["columns"] = "*"
            else:
                tree["columns"] = tokens[1].split(",")
            tree["table"] = tokens[3]
            if "WHERE" in tokens:
                where_index = tokens.index("WHERE")
                tree["where"] = ' '.join(tokens[where_index + 1:])
        return tree

    def interpret(self, tree):
        if tree["command"] == "CREATE":
            self.db.create_table(tree["table"], tree["columns"])
        elif tree["command"] == "INSERT":
            self.db.insert_into(tree["table"], tree["values"])
        elif tree["command"] == "SELECT":
            result = self.db.select_from(tree["table"], tree["columns"], tree.get("where"))
            print(result)


