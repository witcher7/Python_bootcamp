# take user list as input and find the smallest number in it


# list = [76,-4,100,3, 25,-2] 
# output = -4 [ smalles element]

enter = int(input(("Enter your length of list : ")))
list = []
for i in range(enter):
  take = int(input())
  list.append(take)


smallest = list[0]
for i in range(enter):
  if smallest>= list[i]:
    smallest = list[i]

print(list)
print(smallest)


# list = [76,-4,100,3, 25,-2] 
# output = 100 [ largest element]

# before closing the python --> I want you to be good in problem
# solving for the interview 
