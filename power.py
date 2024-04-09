#Write a program that takes an integer as input and returns true if the input is a power of two.
#Examples:
#8=> returns true
#6=> returns false power 2")

def check_power_of_two():

    num = int(input("Enter a number: "))
    if num <= 0:
        print("False")
    else:
        if (num & (num - 1)) == 0:
            print("True")
        else:
            print("False")

check_power_of_two()



