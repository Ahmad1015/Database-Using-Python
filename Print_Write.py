class Print_Write:
    def __init__(self,result,column_names):
        self.result=result
        self.column_names = column_names

    def common_Code(self):
        output = ""
        for column_name in self.column_names:
            size = len(column_name.split(" "))
            if size == 2:
                column, data_Type = column_name.split(" ")
                data_Type = '(' + data_Type + ')'
                output = output+ column + data_Type + "\t"
            if size == 4:
                column, data_Type, primary,key  = column_name.split(" ")
                data_Type = '(' + data_Type + ')'
                primary = '(' + primary +" "+ key + ')'
                output = output + column + data_Type + primary + "\t"
        output = output.rstrip("\t")  # Remove the trailing tab
        output += "\n"

        for row in self.result:
            for item in row:
                output =output+ item+'\t'
            output = output.rstrip("\t")  # Remove the trailing tab
            output += "\n"
        return output
    
    def print(self):
       output = self.common_Code()
       print(output)

    
    def write_tsv(self,table_name):
        table_name = table_name+".txt"
        output = self.common_Code()
        print(output)
        with open(table_name, 'w') as f:
            f.write(output)
        print("Written Successfully to the File")








