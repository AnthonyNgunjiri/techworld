# Write a program to generate the Fibonacci sequence up to 100def fib(n):

def fib_n(limit):
        n = [0, 1]
        while n[-1] + n[-2] <= limit:
            n.append(n[-1] + n[-2])
        return n
# Generating Fibonacci sequence up to 100
fib_n = fib_n(100)
# Printing the generated Fibonacci sequence
print(fib_n)


