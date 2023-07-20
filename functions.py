# *args (arguments)
print("*args".center(50, "=") + "\n")


def multiple_args(*args):
    print(args)             # Retuns a tuple
    print(type(args))


# When there are unknown number of arguments, the function returns *args as a tuple
multiple_args("Dave", "Sara", "John")

# *kwargs (keyword arguments)
print("*kwargs".center(50, "=") + "\n")


def multiple_kwargs(**kwargs):
    print(kwargs)             # Retuns a dictionary
    print(type(kwargs))


# When there are unknown number of keyword arguments, the function returns *kwargs as a dictionary
multiple_kwargs(firstname="Dave", last="Gray")
