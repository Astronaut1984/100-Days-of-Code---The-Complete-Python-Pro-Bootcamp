# Advanced arguments

# default values:
# def fun(a=1, b=2, c=3):
#     code

# *args: Many positional arguments

# Can accept any number of arguments
# def add(*args):
#     for n in args:
#         print(n)
# Args will be treated as a tuple


def add(*args):
    sum = 0
    for num in args:
        sum += num

    return sum


print(add(2, 4, 5, 6))


# **kwargs
# treated as a dictionary


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)
