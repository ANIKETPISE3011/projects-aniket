import string
import datetime as dt
print('Fixer Utilities :\n')
#removing leading or lagging space from a data entry
Baddata= '    Data Science with too many spaces is bad     '
print('Baddata :\n'">",Baddata,"<")
CleanData=Baddata.strip()
print('After Fixing the space ;\n'">",CleanData,"<")

#string.printable()--It is pre-initialized string used as constant
# it gives all the set of punctuation, digits,ASCII values and whitespace
printable=set(string.printable)

BadData1='Data\x00science with x/2 funny character is \x10bad!!!'
print('It will not print all data all the data due to baddata:\n',BadData1)

#filter()--it takes two parameter one is function and second is variable(list)
# we use function so that it can be reusable function but if a function just return a singlevalue in that case we can use lambda.

#lambda()--it takes two parameter one is lambda argument and second is expression
CleanData1=''.join(filter(lambda x:x in string.printable,BadData1))
print('After Cleaning Data:',CleanData1)

print('Reforming Data entry to match specific formating criteria:\n')
print('Convert YYYY/MM/DD to DD/MM/YYYY \n')

#format()--Used to Format string
BadDate=dt.date(2022,10,6)
BadData2=format(BadDate,'%y-%m-%d')
print('BadDate :',BadData2)

#stringtime (time_data,format_data)-- it is used to format time stamp which isin string format to datetime object.
GoodDate=dt.datetime.strptime(BadData2,'%y-%m-%d')

NormalData=format(GoodDate,'%d-%m-%y')
print('NormalDate',NormalData)

GoodData=format(GoodDate,'%d-%B-%y')
print('GoodDate:',GoodData)
