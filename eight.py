# in while loops we dont know when to stop right 
# we dont have any stopping point / range !! 
# In for loops, we can have a range till that we can do the work
# for work in range(11):
#    # work is a variable which will start from 0 (by default till n-1 (9))
#   print("Hi")
#    # 1 2 3 4 5 6 7 8 9 10 --> 10 numbers
#    # 0 1 2 3 4 5 6 7 8 9 10 -->  11 numbers 

# for i in range(3,0,-1):
#                  # -1 as I wanted to go till 0 and reduce -1 
#    print(i)


# print range --> 300 --> 89

# calculate the sum of numbers till n (the user will give the range for that)
# n = 10
# output = 55 ( 1+2+3+4+5+6+7+8+9+10)

# n = 15
# output = ----(( 1+2+3+4+5+6+7+8+9+10 +11+12+13+14+15))

n = int(input("Enter the range you want"))
sum = 0
for i in range(n+1): # because we want to reach n point not n-1 point
  sum = sum + i
  print(sum)

print(sum)

# print the product of numbers till n
n = 10
output = 3628800 ( 1X 2 X 3 X 4 X5 6X7 X8 X 9 X10)
#  10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 3628800.
