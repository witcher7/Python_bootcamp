# ERRORS

# 1. SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.

# name = "Rish"
# if name=="Rish": # anything that you should have written but did not
#  print(name)

# TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer

# ans = "number"
# check = 10
# print(ans + check)

# NameError: This exception is raised when a variable or function name is not found in the current scope.

# def func(a): # a as variable
#  print(b)
#  #I can use a throught my function, but I am using b


# func(10)


# IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.

# list = [ 1 , 2 , 3 , 5 , 10 , 9]
# #        0   1   2   3   4    5
# print(list[6])


# tuple === list
# if we have made anything a tuple.. we cant add or delete
# anything from tuple

# list = [1,2]
# list.append(10)
# print(list)

# tuple = (1 , 2)
#         #0  #1
# print(tuple[1])


# ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.


# ERROR HANDLING
# name = 10000
# try:
#  print(10000/0)
# except ZeroDivisionError:
#    print(1+1)

# Try and except statements are used to catch and handle exceptions in Python. Statements that can raise exceptions are kept inside the try clause and the statements that handle the exception are written inside except clause.

# Example: Let us try to access the array element whose index is out of bound and handle the corresponding exception


# name = "John"
# num = 10
# try:
#  ans = name + num
# except TypeError:
#   print("John 10")

# list = [ 1 , 2 , 3]
# #        0   1   2
  
# try: 
#   print("Second element is " , list[1]) 
#   print("Fourth element is ", list[3])
# except IndexError:
#   print("An error occured as the index is not there")

##################################################
def fun(a):
    if a < 4:
 
        # throws ZeroDivisionError for a = 3
        b = a/(a-3)
 
    # throws NameError if a >= 4
    print("Value of b = ", b)

def fun_new(a):
  print(a)
try:
    # fun(3)
    fun(5)
 
# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
    fun_new(3)
except NameError:
    print("NameError detected and Handled")
    fun_new(5)
