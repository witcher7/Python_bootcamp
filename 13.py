# duplicate in string 
# user = input("Enter your string : ")
# duplicate = ""
# length = len(user)

# for i in range(length-1):
#   for j in range(i+1,length):
#     if user[i]==user[j]:
#        if user[i] not in duplicate:
#           duplicate = duplicate + user[i]

# print(duplicate)

# PRACTICE --> YOU WILL BE COMFORTABLE MORE WITH PYTHON
# THAT"S THE CORRECT PATH YOU ARE ON, IF YOU ARE GETTING PROBLEM IN
# LOGIC, THEN JUST BE PATIENT AS YOU ARE ON CORRECT PATH
# THIS IS HOW LOGIC BUILDING BUILDS

# user enters a string --> Aabra kadabra
# you have to print only even number of index alphabets
#  A a b r a  k a d a b r a
#    0 1 2 3 4  5 6 7 8 9 10 11

# ans = [b,a,a,a,r]

# str = input("Enter the string : ")
# ans = []
# length = len(str)
# for i in range(1,length):
#    if i%2==0: # we are checking even or not
#     ans.append(str[i])

# print(ans)

# Count number of duplicates there in the string
# string = "Aabra kadabra"
# user = "a"
output = 6

string = "Aabra kadabra"
print(string.upper())
print(string.lower())
