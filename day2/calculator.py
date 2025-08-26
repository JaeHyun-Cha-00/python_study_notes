# Let's make a simple calculator

# x = input("What is x? ") # Currently string 
# y = 1

# z = int(x) + y

# print(z)


# x = int(input("What is x? ")) # Currently string 
# y = 1

# print(x+y)


# x = 2
# y = 3

# print(round(x / y, 3))

# def hello(to = "world"):
#     print("hello, ", to)

# hello()

# name = input("What is your name? ")
# hello(name)

def main():
    x = int(input("What is x? "))
    print("x squared is", square(x))

def square(n):
    return pow(n, 2)

main()