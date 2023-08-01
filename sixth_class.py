# n = int(input())
# if n %7==0:
#   print("it is divisible by 7")
# else:
#   print("It is not divisible by 7")

# how to find last digit of a number --> 
# number = 4569
# last_digit = 4569%10 ---> 9 as the last last_digit
#             last_digit /10 --> 456 (the remaining number after last digit)
#             456 %10 --> 6 as the last last_digit    
#             last_digit /10 --> 45
#            45 %10 --> 5 as the last last_digit


# LOOPS -->means doing something again, again and again


# you want to print numbers from 10 --> 1
# n = 10
# while n >0:
#   print(n) # [10] [n = 9(n-1)] [ n =8 [n-1]].......[n =0 ]
#   # n = n-1 
n = 0
while n <=10:
  
  n = n +1
  if n==6:
    break # it will just avoid the 6th position
  print(n)

# break means breaking the loop
# continue means ---> skip the next line and continue from starting




# I want to reverse a number
# input : 45 6   9 --> output:9654

n = int(input("Enter your number : "))
reverse = 0
while n >0:
  last_digit = int(n%10) # module
  reverse = reverse *10 + last_digit  # ans = 0*10 + 9  , ans = 9*10 + 6 = 96*10 + 5,965
  n = int(n /10)

print(reverse)
