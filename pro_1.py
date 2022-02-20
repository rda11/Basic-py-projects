from tkinter.messagebox import YES
from cupshelpers import Printer


print("welcome to Quiz Game!")

play = input("do you wanna play? ")

if play.lower()  != "yes":
    print("ok Bye")
    quit()

print("let's play")
Point = 0

answer = input("1) what is ROS full form? ")

if answer.lower()  == "robot operating system":
    print("Correct")
    Point+=1
else:
    print("Incorrect")   

answer = input("2) what is CV full form? ")

if answer.lower()  == "computer vision":
    print("Correct")
    Point+=1
else:
    print("Incorrect")

answer = input("3) what is CNN full form? ")

if answer.lower()  == "convolutional neural network":
    print("Correct")
    Point+=1
else:
    print("Incorrect")

answer = input("4) what is AI full form? ")

if answer.lower() == "artificial intelligence":
    print("Correct")
    Point+=1
else:
    print("Incorrect") 

answer = input("5) what is OOPs full form? ")

if answer.lower() == "object oriented programming":
    print("Correct")
    Point+=1
else:
    print("Incorrect") 

print("Your Point is " + str((Point/5)*100) + "%")
