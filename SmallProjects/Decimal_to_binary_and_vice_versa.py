try:
    menu=int(input("Choose an option : \n 1. Decimal to Binary \n 2. Binary to Decimal\n Option: "))
    if menu < 1 or menu > 2:
        raise ValueError
    if menu == 1:
        dec = int(input("Input your decimal number:\n Decimal: "))
        print("Binary: {}".format(bin(dec)[2:]))
        
    elif menu == 2:
        binary=input("Input your binary number:\n Binary: ")
        print("Decimal: {}".format(int(binary, 2)))
        
except:
    print("Please choose a valid option")            