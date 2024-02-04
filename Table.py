from Column import Column as cl
class Table:
    def __init__(self,table_name):  # Column names is a list of string whereas table name is just a string
        self.table_name = table_name
        self.columns = []
        self.rows=[]

    def set_column_names(self,column_names,data_types):
        for i,column_name in enumerate(column_names):
            column = cl(column_name,i,data_types[i])
            self.columns.append(column)


    def insert_row(self,data):
        self.rows.append(data)

    def return_row(self):
        index = 0            # Check where
        return self.rows[index]

    def update_row(self,data):
        index = 0            # Check where
        self.rows[index] = data

    def delete_row(self):
        index = 0           # Check where
        return self.rows.pop(index)

    def display_table(self):
        for element in self.columns:
            print(element.get_name(),end="\t")
