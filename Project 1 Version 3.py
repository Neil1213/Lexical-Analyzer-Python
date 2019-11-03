import sys
#Printing required information
print("Project 1 for CS 341")
print("Semester: Fall 2018")
print("Written by: Neil Shah, ns642")
print("Instructor: Marvin Nakayama, marvin@njit.edu")

#Begin the input loop for taking input until user enters 'y'
while True:
    #Asking user if they want to enter a string
    userIn = input("Do you want to enter a string (y or n): ")
    #If user inputs 'n' then the program terminates
    if(userIn == 'n'):
        sys.exit()
    #Additional step to ensure that user only inputs 'y' or 'n'
    if(userIn!='y'):
        print("Invalid response")
        continue
    #Getting the string from the user
    userIn = input("Enter a string: ")

    #english Alphabet
    Gamma = "abcdefghijklmnopqrstuvwxyz"
    #Alphabet of Language L
    Sigma = Gamma + "."
    #Storing the result of DFA
    result = "accepted"
    #Printing the user entered string
    print("You entered: ", userIn)

    #Tracking the states of DFA
    counter = 0
    #Tracking the lenght of the input
    inputLen = 0
    #Begin DFA
    for letter in userIn:
        counter+=1
        inputLen+=1
	#DFA Q1 State
        if(counter == 1):
            if(letter == "w"): print("Current State: Q"+str(counter)+ " Letter read: "+letter)
            elif(letter == "."):
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
                result = "Rejected"
		#Going to trap state
                counter = 16
            else:
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
                counter = 8
	#DFA Q2 State
        elif(counter == 2):
            if(letter == "w"): print("Current State: Q"+str(counter)+ " Letter read: "+letter)
            elif(letter == "."):
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
                counter = 9
            else:
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
                counter = 8
        #DFA Q3 State
	elif(counter == 3):
            if(letter == "w"): print("Current State: Q"+str(counter)+ " Letter read: "+letter)
            elif(letter == "."):
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
                counter = 9
            else:
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
                counter = 8
	#DFA Q4 State
        elif(counter == 4):
            if(letter == "."): print("Current State: Q"+str(counter)+ " Letter read: "+letter)
            else:
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
                counter = 8
	#DFA Q5 State
        elif(counter == 5):
            if(letter == "c"): print("Current State: Q"+str(counter)+ " Letter read: "+letter)
            elif(letter == "."):
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
                #Going to trap state
		counter = 16
                result = "Rejected"
            else:
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
                counter = 8
	#DFA Q6 State 
        elif(counter == 6):
            if(letter == "o"):
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
                result = "Accepted"
            elif(letter == "."):
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
                counter = 9
            else:
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
                counter = 8
        #DFA Q7 State (Acceptance State)
	elif(counter == 7):
            if(letter == "m"):
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
                result = "Accepted"
            elif(letter == "."):
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
                counter = 9
            else:
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
                counter = 8
        #DFA Q8 State (Acceptance State)
	elif(counter == 8):
            if(letter == "."):
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
                counter = 9
            else:
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
        #DFA Q9 State
	elif(counter == 9):
            if(letter in Gamma):
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
                counter = 8
            else:
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
        #DFA Q10 State
	elif(counter == 10):
            if(letter == "c"):print("Current State: Q"+str(counter)+ " Letter read: "+letter)
            else:
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
		#Going to trap state
                counter = 16
                result = "Rejected"
        #DFA Q11 State 
	elif(counter == 11):
            if(letter == "o"):
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
                result = "Accepted"
            else:
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
		#Going to trap state
                counter = 16
                result = "Rejected"
	#DFA Q12 State (Acceptance State)
        elif(counter == 12):
            if(letter == "m"):
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
                result = "Accepted"
            else:
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
		#Going to trap state
                counter = 16
                result = "Rejected"
	#DFA Q13 State (Acceptance State)
        elif(counter == 13):
            if(letter == "."): print("Current State: Q"+str(counter)+ " Letter read: "+letter)
            else:
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
		#Going to trap state
                counter = 16
                result = "Rejected"
       #DFA Q14 State
       elif(counter == 14):
            if(letter == "c"):print("Current State: Q"+str(counter)+ " Letter read: "+letter)
            else:
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
		#Going to trap state
                counter == 16
                result = "Rejected"
        #DFA Q15 State 
	elif(counter == 15):
            if(letter == "o"):
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
                result = "Accepted"
            else:
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
        #Going to trap state
		counter == 16
                result = "Rejected"
        #DFA Q16 State (Acceptance State)
	elif(counter == 16):
            if(letter in Sigma):
                print("Current State: Q"+str(counter)+ " Letter read: "+letter)
                result = "Rejected"
        #DFA Q17 State (Trap State) 
	elif(counter == 17):
            print("Current State: Q"+str(counter)+ " Letter read: "+letter)
	    #Going to trap state
            counter = 16
            result = "Rejected"

    #Printing the finish state of DFA and whether the string is rejected or accepted
    print("Current State: Q" + str(counter+1)+"\n"+result)
