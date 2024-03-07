stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

caret = stdform.find("^")
exponent = stdform[caret + 1:]
multiply = stdform.find("x")
significand = stdform[:multiply]
print("This number in E notation is", significand + "E" + exponent + ".")

# Type your code below
