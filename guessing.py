import random

ip = input("Type a number: ")

if ip.isdigit():
    ip = int(ip)

    if ip <= 0:
        print("Type a valid number")

else:
    print("Type number")
    quit()

random_no = random.randint(0, ip)

guesses = 0
while True:
    guesses+=1
    user = input('Guess a number: ')
    if user.isdigit():
        user = int(user)
    else:
        print("Go for next time")
        continue
    if user == random_no:
        print("Correct")
        break
    elif user > random_no:
        print('Your guess is bigger')
    else:
        print('your guess is smaller')
print("you got it in ", guesses, "guesses")