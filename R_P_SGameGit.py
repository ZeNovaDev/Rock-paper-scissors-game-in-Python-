import random

computer_points=0
user_points=0
rps_emojis={"r":"🪨", "p":"📃", "s":"✂️"}
print("Welcome to the Rock paper scissors game")
choices = ("r", "p", "s")
while True:
  Continue=input("Would you like to play or quit? (p/q): ").lower()
  if Continue=="p":
    user_choice = input("Rock/paper/scissors? (r/p/s): ")
    if user_choice not in choices:
      print("Invalid choice")
      continue
    computer_choice=random.choice(choices)
    print(f"you chose {rps_emojis[user_choice]} ")
    print(f"Computer chose {rps_emojis[computer_choice]} ")
    if   user_choice==computer_choice:
      print("Tie")
      print("+0 points")
    elif (
(user_choice=="r" and computer_choice=="s") or (user_choice=="s" and computer_choice=="p") or (user_choice=="p" and computer_choice=="r")):
      print("you won,congrats")
      user_points+=1
      print("+1 points to you")
      print(f"You have {user_points}")
      print(f"Computer have {computer_points}")
    else:
      print("you lose")
      computer_points+=1
      print("+1 points to computer")
      print(f"You have {user_points}")
      print(f"Computer have {computer_points}")
      
    continue
  elif Continue=="q":
    print("Thanks for playing :) ")
    break
    
    
                   
                                                 