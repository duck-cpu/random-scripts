import random

#We are creating a random even number between 2 and 10
#by first randomizing an integer between 1 and 5.
#This will be our final number and multiply it by 2.

randomFinalNumber = random.randrange(1, 5)
numberToAdd = randomFinalNumber * 2

#ask user their name

name = input("hello, what is your name? ")
print("Welcome " +name +", we’ll perform some mind reading on you.")
print("First, think of a number between 1 and 10.")
answer = input("Ready for the next step? ")
print("Multiply the result by 2.")
answer = input("Ready for the next step? ")
print("Now, add...let's see...")
print(numberToAdd)
answer = input("Ready for the next step?")
print("Now, divide the number you have by 2.")
answer = input("Ready for the next step? ")
print("Now, subtract the original number that you thought about.")
answer = input("Ready for the last step? ")

print("Well " +name +", let me read your mind...The number that you have right now is a....")
print(randomFinalNumber)