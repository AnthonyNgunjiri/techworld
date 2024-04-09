#Write a program that takes an integer as input and returns an integer with reversed digit
#ordering.
#Examples:
##For input 500, the program should return 5.
#For input -56, the program should return -65.
#For input -90, the program should return -9.
#For input 91, the program should return 19.
# Step 1: Immediately prompt the user for input as the program starts
user_input = input("Enter an integer: ")
num = int(user_input)
def reverse_integer(num):
    if num < 0:
        num_str = str(num)[1:]
        reversed_str = '-' + num_str[::-1]
    else:
        reversed_str = str(num)[::-1]
    return int(reversed_str)


reversed_num = reverse_integer(num)
print(f"The reversed integer is: {reversed_num}")



