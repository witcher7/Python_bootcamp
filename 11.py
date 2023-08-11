length = int(input("Enter the length of the list: "))
list = []
for i in range(length):
  take = int(input()) # here we are taking input
  list.append(take)  # we are storing that input

print(list)
max = 0
for i in range(length):
  if max <= list[i]:
     max = list[i]

print(max)
