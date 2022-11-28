#python program to illustrate
#finding common member in list
#without using operators
#define a finction that takes two lists
def overlapping(list1,list2):
    for i in range(0,len(list1)):
        for j in range(0,len(list2)):
            if (list1[i]==list2[j]):
                return 1
            return 0

list1=[1,2,3,4]
list2=[1,2,3,4]
if (overlapping(list1,list2)):
    print('Overlapping!')
else :
    print('Not overlapping!')
                       
