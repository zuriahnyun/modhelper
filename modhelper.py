#Author: Zuriahn Yun
#Date: January 27th 2023
#Modulo Helper to help gain understanding of the modulo operator

#Comand line Inputs
import sys
if len(sys.argv)> 1:
    first = (sys.argv[1])
    second = (sys.argv[2])

else:
#Input for two variables you want to use
    first = int(input("Enter the first number:"))
    second = int(input("Enter the second number:"))

#Questions with the two inputed variables
print("What is ", first , " mod ", second,"?", sep="")
response1 = int(input())
print("What is ", second, " mod ", first,"?", sep="")
response2 = int(input())

#Correct answers and remainders and score value
correct1 = first % second 
correct2 = second % first
divided1 = first // second
divided2 = second // first
score = 0

#If else statments to print correct answers and add points
if response1 == correct1:
    score +=1
    print("Awesome!")
elif response1 != correct1:
    print("Aw")
print(first, "divided by", second, "is", divided1, "remainder", correct1)
if response2 == correct2:
    score +=1
    print("Awesome!")
elif  response2 != correct2:
    print("Aw")
print(second, "divided by", first, "is", divided2, "remainder", correct2)

#Printing final score 
print("Your score is", score, "out of 2.")