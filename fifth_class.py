import random
computer_choice = random.randint(1,3)
user_choice= input("Enter your choice : Rock / Paper / Scissor : ")

if user_choice=="Rock" or user_choice=="rock":
  if computer_choice==1:  # 1 stands for paper
    print("You Lose as Computer's choice is Paper")
  elif computer_choice ==2: # 2 stands for Scissor
    print("You win as Computer's choice is Scissor")
  else:
    print("It is Tie! as Computer's choice is Rock")

elif user_choice=="Paper" or user_choice=="paper":
  if computer_choice==1:  # 1 stands for paper
    print("It's a Tie! as Computer's choice is Paper")
  elif computer_choice ==2: # 2 stands for Scissor
    print("You lose as Computer's choice is Scissor")
  else:
    print("You win as Computer's choice is Rock")

elif user_choice=="Scissor" or user_choice=="scissor":
  if computer_choice==1:  # 1 stands for paper
    print("You win as Computer's choice is Paper")
  elif computer_choice ==2: # 2 stands for Scissor
    print("Tie as Computer's choice is Scissor")
  else:
    print("You lose  as Computer's choice is Rock")

else:
  print("Invalid Option has been choosed")
