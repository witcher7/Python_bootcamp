# # list = [1,2,3,45,60]
# # print(list)
# # length = len(list)
# # #I want to print elements one by one
# # # for loop

# # for x in range(length):
# #    print(list[x]) # list[0]..list[1]...list[2]....list[3] ..list[4]


# # # this is how we usually save our data in list = []

# # I want anyone can save the numbers in the list
# length = int(input("Enter the length of the list: "))
# list = []
# for i in range(length):
#   take = int(input()) # we will take inputs for our list
#   list.append(take) # we are putting back the element in the list

# print(list)

# Rock paper scissor game
import random
computer_choice = random.randint(1,3) # 1--> rock, 2 --> paper, 3 --> scissors
human_choice=input("Enter your choice Rock/ Paper/ Scissors : ")

if human_choice=="Rock": # ROCK
  if computer_choice==3:
     print("Hey you won !! as the computer's choice is Scissors")
  elif computer_choice==2:
     print("Hey yoy Lose !! as the computer's choice is Paper")
  else:
     print("It's a tie")

elif human_choice=="Paper": # Paper 
   if computer_choice==3:
     print("Hey you Lose !! as the computer's choice is Scissors")
   elif computer_choice==1:
     print("Hey you Won !! as the computer's choice is Rock")
   else:
     print("It's a tie")

elif human_choice=="Scissors": #Scissors
  if computer_choice==1:
     print("Hey you Lose !! as the computer's choice is Rock")
  elif computer_choice==2:
     print("Hey you Won !! as the computer's choice is Paper")
  else:
     print("It's a tie")
