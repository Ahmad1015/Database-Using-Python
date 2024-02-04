class Print_Write:
    def __init__(self,result,column_names):
        self.result=result
        self.column_names = column_names
    
    def common_Code(self):
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
        
        return output
    
    def print(self):
       output = self.common_Code()
       print(output)

    def write_tsv(self,table_name):
        table_name = table_name+".txt"
        table_name = "E:\\Database Management System\\Database\\temp\\temp write\\"+ table_name
        output = self.common_Code()
        with open(table_name, 'w') as f:
            f.write(output)








