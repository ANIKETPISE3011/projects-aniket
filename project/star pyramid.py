#python  code to demonstrate star pattern using name.
# function to demonstrate printing pattern.
def pyramid(n):
    #outer loop to handle number of rows
    #n in the case
    for i in range(0,n):
        #inner loop to handle number of columns
        #values changing acc. to outer loop
        for j in range(0,i+1):
            #printing name
             print('ANIKET', end=',')
        #ending line after each row
        print('\r')
pyramid(10)
