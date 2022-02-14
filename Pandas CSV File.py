# import pandas as pd
# data=pd.read_csv("PandasCSV.csv")
# print(pd)
# print(data)

# import pandas as pd
#
# # creating a data frame
# df = pd.DataFrame([[1,'Jack', 567], [2,'Rose', 222]], columns = ['Sno','Name', 'Age'])
#
# # writing data frame to a CSV file
# df.to_csv('PandasCSV.csv')

# import pandas
# df = pandas.read_csv('PandasCSV.csv', index_col='Sno')
# print(df)
#
# import pandas
# df = pandas.read_csv('PandasCSV.csv', header=0,names=['Serial no', 'Employee name', 'Employee age'])
# print(df)

# Inheritance in CSV
# import module
import csv

class Employee:

    def employeeDetails(self):
        with open('data.csv', newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in data:
                print(', '.join(row))


class Department(Employee):

    def departmentDetails(self):
        super()

        with open('department.csv', newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in data:
                print(', '.join(row))


# object of Manager class
obj = Department()

# output
print("-----Employee Detail-----")
obj.employeeDetails()

print("-----Department Detail-----")
obj.departmentDetails()
