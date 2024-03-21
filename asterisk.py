# Multiplication operator
print(4 * 5)
print(3 * "Hello ")

# Unpacking operator
a, b, *others = (4, 5, 12, 4, 5, -2)
print("a = %s, b = %s, others = %s" % (a, b, others))


# Allow any number of positional arguments
def say_hello(*args):
    print(args)


say_hello("Choaib", 22, "ENSA")


# Allow any number of keyword arguments
def say_hi(**kwargs):
    print(kwargs)


say_hi(name="Choaib", age=22, school="ENSA")
