#here we are programing a code for decimal to binary converter and viceversa.
try:
#here we are giving two option 1 for decimal to binary and 2 for binary to decimal. 
    menu = int(input("Choose an option: \n 1. Decimal to binary \n 2. Binary to decimal\n Option: "))
    if menu < 1 or menu > 2:
# here if a function receives an argument of a correct type but inappropriate value it will raise a valueerror
       raise ValueError
    if menu == 1:
        dec = int(input("Input your decimal number:\nDecimal: "))
        print("Binary: {}".format(bin(dec)[2:]))
    elif menu == 2:
        binary = input("Input your binary number:\n Binary: ")
        print("Decimal: {}".format(int(binary, 2)))
except ValueError:
    print ("please choose a valid option")

