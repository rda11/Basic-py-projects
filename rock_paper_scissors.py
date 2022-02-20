import random

user_win = 0
computer_win = 0

options = ["rock", "paper","scissor"]

while True:
    user_ip = input('Type Rock/Paper/Scissor or type Q to quit:  ').lower()
    if user_ip == "q":
        break
    if user_ip not in options:
        print("Inalid response")
        continue

    random_number = random.randint(0,2)

    computer_answer = options[random_number]
    print("computer picked", computer_answer)

    if user_ip == "rock" and computer_answer == "scissor":
        print("you win")
        user_win+=1
    elif user_ip == "scissor" and computer_answer == "paper":
        print("you win")
        user_win+=1
    elif user_ip == "paper" and computer_answer == "rock":
        print("you win")
        user_win+=1
    elif user_ip == computer_answer:
        print("same")

    else:
        print("you lost")
        computer_win+=1


print("you won", user_win, "times.")     
print("computer won", computer_win, "times.")    
print("Bye")