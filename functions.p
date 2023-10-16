# We were writing piece of code
# But let's suppose I want to write the code 
# in a piece / block so that I can use whenever I can

# def name():
#   print("Hello Kangeshan")

# # We have to call our function to work
# name()

# If we dont call our name of the function it will not run
# And we have to call our function to work

from new import cup
# from the filename import the function name

# there can be multiple files
# cup()

# def anyname():# the space says the work is under the function
#   for i in range(10): 
#     print(i) # this print statement will only run if
#     # it is a part of for loop / it is not a part of function
#   print("Hello")
#   print("Hi kangeshan")

# def addition(a,b): # I am recieving the value from function call
#   # I want to send the values to functions so that it can work on them
#   print(a+b)


# a = int(input("Enter your value: "))
# b = int(input("Enter your value: "))
# # I have saved the values in a and b
# addition(a,b) # I am sending the values
# # here is the function call

# we are changing the values in function
# Virtual world
def value(a,b):
  a = 20
  b = 30
  return a,b  # I am returing some value to my real world

a = int(input("Enter your value: "))
b = int(input("Enter your value: "))
ans = value(a,b)
# because answer is storing values directly --> tuple
# I need some person to recieve the value
print(ans)
