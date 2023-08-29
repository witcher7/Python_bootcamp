# file = open('new.txt','r')
# # variable = open (' name of the file', 'r for read')

# print(file.read())
# # we are printing ( variable.read())
#                      # to read and print the file


# dogs = open('breeds.txt','r')
# # print(dogs.read())
# print(dogs.readline(5)) |
# print(dogs.readline(5)) |
# print(dogs.readline(5)) |  # it is going down and wrapping the names
#                         V
# # it will print first 5 characters in the list



# we are reading before deleting and writing
dogs = open('breeds.txt','r')
print(dogs.read())

dogs = open('breeds.txt','w') # this will delete previous data
dogs.write("breed100") # new data will be added

# now to see new data, we need to read the file after adding the new
# data
dogs = open('breeds.txt','r')
print(dogs.read())
