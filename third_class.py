#if and else 
# it helps in telling different situations

#  # = , it means we are assigning the value
# name = input("Enter the name : ")
# if name =="Louis Vuiton":  # == to check whether n has a value of 10 or not
#     print("the name is a luxury brand")
# else:
#    print("it is just a normal name")




# if --> line 3
# print() line 4


# if --> line 3
#   print() --> line 3.1 (which will only run if line3 is working)



# RIGHT NOW, We only have two possibilites

# n = int(input())
# if n ==10:
#   print(10)
# elif n ==20:  # else if==> providing a new possibility
#   print(20)
# elif n ==30:
#   print(30)
# else:
#   print("Any other random number")


# I want to check if the user has entered even or odd number
# N /2 and is giving 0 as remainder ( it is even)
# 4/2 --> 0 ( we are asking for remainder)
# 3/2 --> 1 ( remainder is there, it will be an odd )
# number = int(input("Enter your number : "))
# if number%2==0:  #(if number is divided by 2 and giving remainder is 0 )
#   print("Number is even")
# else:
#   print("Number is odd")

# lottery checker
number = int(input("Enter your lottery number sir : "))
lottery = 3410976
if number==lottery:
  print("Congratulations, you won 1 million USD$ :) ")
else:
  print("SORRY !! better luck next time")

