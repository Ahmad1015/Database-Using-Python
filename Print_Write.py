class Print_Write:
    def __init__(self,result,column_names):
        self.result=result
        self.column_names = column_names

    def print(self):
        # Calculate the maximum length of data in each column
        max_lengths = [max([len(str(item)) for item in
                            [column.split(" ")[0] + '(' + column.split(" ")[1] + ')'] + [row[i] for row in
                                                                                         self.result]]) for i, column in
                       enumerate(self.column_names)]

        # Print the top border
        print("+" + "+".join(["-" * (length + 2) for length in max_lengths]) + "+")

        # Print the header with the column names
        for i, column_name in enumerate(self.column_names):
            column, data_Type = column_name.split(" ")
            data_Type = '(' + data_Type + ')'
            print("| " + (column + data_Type).ljust(max_lengths[i]) + " ", end="")
        print("|")

        # Print the border between the header and the data
        print("+" + "+".join(["-" * (length + 2) for length in max_lengths]) + "+")

        # Print each row of data
        for row in self.result:
            for i, item in enumerate(row):
                print("| " + str(item).ljust(max_lengths[i]) + " ", end="")
            print("|")

            # Print the border between each row
            print("+" + "+".join(["-" * (length + 2) for length in max_lengths]) + "+")

    def write_tsv(self,table_name):
        table_name = table_name+".txt"
        output = ""
        for column_name in self.column_names:
            column, data_Type = column_name.split(" ")
            data_Type = '(' + data_Type + ')'
            output = output+ column + data_Type + "\t"
        output = output.rstrip("\t")  # Remove the trailing tab
        output += "\n"

        for row in self.result:
            for item in row:
                output =output+ item+'\t'
            output = output.rstrip("\t")  # Remove the trailing tab
            output += "\n"
        print(output)
        with open(table_name, 'w') as f:
            f.write(output)








