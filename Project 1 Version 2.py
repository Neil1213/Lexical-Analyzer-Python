import sys

#print required text
print("Project 1 for CS 341")
print("Semester: Fall 2018")
print("Written by: Neil Shah, ns642")
print("Instructor: ,Marvin Nakayama, marvin@njit.edu")



while True:
    #Asking if a user want to enter a string
    userIn = input("Do you want to enter a string (y or n): ")

    #Processing user input
    if(userIn == 'n'):
        sys.exit()
    if(userIn!='y'):
        print("Invalid response")
        continue
    userIn = input("Enter a string: ")
    #Setting the alphabet for L
    Gamma = "abcdefghijklmnopqrstuvwxyz"

    #Setting the status variable
    result = "accepted"

    #Printing user inputted string
    print("You entered: ", userIn)

    #Setting the variable for different states
    counter = 2

    #Setting value for length for user input
    inputLen = 0
    #Go through DFA
    print("Q1")
    for letter in userIn:
        inputLen+=1
        if(counter<=4):
            if(letter == "w"):
                print("Q", counter," ",letter, sep="")
                counter+=1
            else:
                result = "rejected"
                break
        elif(counter==5):
            if(letter == "."):
                print("Q", counter, " ", letter, sep="")
                counter+=1
            else:
                result = "rejected"
                break
        elif(counter==6):
            if (letter in Gamma):
                print("Q", counter, " ", letter, sep="")
                continue
            elif(letter == "."):
                print("Q7", letter)
                counter+=2
        
        elif(counter==8):
            if(letter=="c"):
                print("Q", counter, " ", letter, sep="")
                counter+=1
            else:
                result = "rejected"
                break
        elif(counter==9):
            if(letter=="o" and len(userIn)==inputLen):
                print("Q14", letter)
                result = "accepted"
                break
            elif(letter=="o"and len(userIn)==(inputLen+1)):
                print("Q", counter, " ", letter, sep="")
                counter+=1
            elif(letter=="o" and len(userIn) > inputLen):
                print("Q", counter+1, " ", letter, sep="")
                counter+=1
            else:
                result = "rejected"
                break
        elif(counter==10):
            if(letter=="m" and len(userIn)==inputLen):
                print("Q14", letter)
                result = "accepted"
                break
            elif(letter!="m"):
                result = "rejected"
                break
            else:
                print("Q", counter+1, " ", letter, sep="")
                counter+=2
        elif(counter==11):
            print("Q", counter, " ", letter, sep="")
            counter+=1
        elif(counter==12):
            print("Q", counter, " ", letter, sep="")
            counter+=1
        elif(counter==13):
            print("Q", counter, " ", letter, sep="")
            counter+=1
        elif(counter==14):
            print("Q", counter, " ", letter, sep="")
            result="accepted"
    if(result=="rejected"):
        for i in range(inputLen-1,len(userIn)):
            print("Q15 ", userIn[i])
    print("String is ", result)
               
