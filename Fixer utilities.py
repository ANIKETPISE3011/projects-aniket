import string
import datetime as dt


print('Fixer utilities : \n')
print('Removing unwanted space from data:\n')
# removing leading or lagging space from a data entry
Baddata= '     data science with too many space is bad     '
print('Baddata : \n ''>',Baddata,'<')
Cleandata= Baddata.strip()
print(' After fixing the space :\n''>',Cleandata,'<')

print('*******************************************************************************************************************************')
print('Removing nonprintable character from a data entry:\n')
# string.printable()-- it is pre -initiallized string used as constsnt
#it gives all the sets of punctuations,ArithmeticError digits,ASCII values and whitespaces
printable=set(string.printable)
Baddata1='Data\x00science with x\2 funny character is \x10bad!!!'
print('it will not print all the data due to Baddata1 :\n',Baddata1)

#filter()--it takes two parameter one is function and other is variable
#we use function so that it can be reusable function but if a function just return a single values in that case we can use lambda

#lambda()--it takes two parameter one is lambda argument and second is expression
Cleandata1=''.join(filter(lambda x:x in string.printable, Baddata1))
print('\n After cleaning the data:', Cleandata1)

print('********************************************************************************************************************************')
print('Removing data entry to match specific formatting criteria:\n')
print('Convert YYYY/MM/DD to DD/MM/YYYY\n')

#format--used to format string
Baddate=dt.date(2022,10,6)
Baddata2=format(Baddate,'%y-%m-%d')
print('Baddata2:',Baddata2)

#strptime(time_data,format_data)--it is used to format time stamp which is in the string format to determine object.
GoodDate=dt.datetime.strptime(Baddata2,'%y-%m-%d')

Normaldata=format(GoodDate,'%d-%m-%y')
print('Normaldata:',Normaldata)

Gooddata=format(GoodDate,'%d-%B-%y')
print('GoodDate:',Gooddata)
