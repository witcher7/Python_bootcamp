# how to take a list from user
# list = [1,2,3,4,5] # right now I am making this list
# but I want anyone can make this list


# length = int(input("Enter the length of the list: "))
# list = []
# for i in range(length):
#   take = int(input()) # take element from the user
#   list.append(take) # put that element inside the list


# print(list)




# whenever you want to solve any question you have to used this part of
# the code to take list from the user

# if the user enters k = 10, you have to find whether this k is there
# in the list or not

# list = [3,-5,10,100,-20,4]
# k = 1
# output -> 

# length = int(input("Enter the length of the list: "))
# list = []
# for i in range(length):
#   take = int(input()) # take element from the user
#   list.append(take) # put that element inside the list


# print(list)

# k = int(input("Enter value for K : "))

# for i in range(length):
#    if k == list[i]: # i ==> 0, length-1
#       print("We have k in our list")
#       break

# list = [ 1,4,5,10,-1,4,2]
# output = 4


length = int(input("Enter the length of the list: "))
list = []
for i in range(length):
  take = int(input()) # take element from the user
  list.append(take) # put that element inside the list

print(list)
duplicate =[]
for start in range(length-1):
  for end in range(start+1,length):
     if list[start]==list[end]:
       duplicate.append(list[start])


print(duplicate)



# REVERSE THE LIST 
Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}

Input :  arr[] = {4, 5, 1, 2}
Output : arr[] = {2, 1, 5, 4}
 
