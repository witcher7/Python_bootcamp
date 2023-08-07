# In while loop -->wedont know when to stop 
#  we are not specifying any kind of limit

# for loop we can specify the range and the limit as well
# for yusif(variable) in range(10): # we define the range at which the loop
#  print(i)                             # by default , variable starts from0
# for yusif in range(10):
#   print(yusif)

# from 5
# for yusif in range (5,11): # range is there till n-1 (10 --> 9 , 11 -->)
#    print(yusif)                       # 5 6 7 8 9 


# I want to do opposite --> 10 --1
# for yusif in range(10,-1,-1):
#   print(yusif)

# 
# 143 --> reverse this number 
# n = 143
# while n>0:
#   rem = int(n%10) # it will give me last number
#   n = int(n/10) # it will remove the last number from n so that we can get our second last number again......
#   print(rem)

# # reverse the number -->  143 --> 341

n = 143
ans = 0
while n>0:
  rem = int(n%10) # it will give me last number
  n = int(n/10) # it will remove the last number from n so that we can get our second last number again......
  ans = ans *10 + rem
        0+ 3 =3 * 10 + 4 = 34* 10 + 1 = 341

print(ans)
