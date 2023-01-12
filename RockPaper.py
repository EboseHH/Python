# Basically, the randint() method in Python returns a random integer value between the two lower and 
# higher limits (including both limits) provided as two parameters.
from random import randint

# The computer needs to be able to select a random item from the list of strings stored in the variable "moves"

moves = ["rock", "paper", "scissors"]
objects = ['rock', 'paper', 'scissors', 'cancel']

response = ""
computer = moves[randint(0,2)]

while response not in objects:
  print("Choose object. Type in one of the following:")
  print(objects)
  response = input(">>> ").lower()

  if response == computer:
    print ("It's a tie")
  elif response == "rock" and computer == "paper":
    print("You lose")

  elif response == "scissors" and computer == "paper":
    print("You win")
  
  elif response == "rock" and computer == "scissors":
    print("You win")

  elif response == "paper" and computer == "rock":
    print("You win")
    
  elif response == "scissors" and computer == "rock":
    print("You lose")
    
  elif response == "paper" and computer == "scissors":
    print("You lose")
    