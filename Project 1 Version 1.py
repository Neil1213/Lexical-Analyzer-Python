import sys
#print required text
print("Project 1 for CS 341")
print("Semester:  Fall 2018")
print("Written by: Neil Shah, ns642")
print("Instructor: Marvin Nakayama, marvin@njit.edu")
#Asking user for input
userIn = input("Do you want to enter a string (y or n): ")
#Processing user's input
if(userIn == "y"):
    userIn = input("Enter a string: ")
elif(userIn == "n"):
    sys.exit()
#Print user's string

alpha = "abcdefghijklmnopqrstuvwxyz"
result = "accepted"
print("You entered:",userIn)
counter = 1
# Go through DFA
# q1
for letter in userIn:
    if(counter<=3):
        if(letter == "w"):
            print("q",counter," ",letter, sep="")
            counter+=1
        else:
            result = "rejected"
            print("q", letter)
            continue
    elif(counter == 4):
        if(letter=="."):
            print("q",counter," ",letter, sep="")
            counter+=1
        else:
            result = "rejected"
            print("q", letter)
            continue
    elif(letter in alpha):
        if(counter==5):
            print("q",counter," ",letter, sep="")
        else:
            counter+=1
            print("q",counter," ",letter, sep="")
    elif(letter == "."):
        counter+=1
        print("q",counter," ",letter, sep="")
        
print(result)
    
