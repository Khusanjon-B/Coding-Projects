import time
import random

#Variable to store values for operations
myList = list(range(1000))

#Changes the list from 0-999 to 1-1000
for i in myList:
    myList[i] += 1
    

#Lists to store values for first and second numbers in equation
gameList1 = []

gameList2 = []

#Variables to keep track of score statistics
score = 0
streak = 0
totalQ = 0
totalR = 0
rounds = 0
playAgain = True

#Variable to track time
timer = 0

#Function to reset variables in order to start new round
def resetVariables():
    
    
    
    gameList1 = []
    
    gameList2 = []
    
    score = 0
    streak = 0
    totalQ = 0
    totalR = 0
    timer = 0
    userInput = ""
    inputStore1 = ""
    
    for i in inputCheck:
        inputCheck[i] = False
    
    gameInfo["Operator"] =""
    gameInfo["Number"] = ""
    
    gameInfo["Up To Number"] = ""
    gameInfo["Number Limit Type"] = ""
    gameInfo["Add/Sub Up To"] = ""

def resetInputChecks():
    for i in inputCheck:
        inputCheck[i] = False

#Key Value Pairs to Store Game Round type
gameInfo = {"Operator":"", "Number":"", "Up To Number":"", "Number Limit Type":"", "Add/Sub Up To":""}

#Lists to store Round Statistics
roundGameInfo = list() #"Operator": "M", "Number" : 10, etc
scoreList = list() #Scores 50, 60, 75, etc.
totalQList = list() #Questions 14, 20, 34, etc.
totalRList = list() #Correct 14, 20, 34, etc.
streaksList = list() #Streaks 14, 20, 34, etc.
timerList = list() #Timers 60, 100, 200, etc.

#Variable to track userInputs
userInput = "========"
inputStore1 = ""
inputStore2 = "" #Stores upto or only value

#Variable to keep input validity check record
#[Integer Check, 0 value check, Under 1000 check, ]
inputCheck = [False, False, False, False]

#Game Start
print("\nWelcome to the math game!")

while playAgain == True:
    
    resetVariables()
    
    score = 0
    streak = 0
    totalQ = 0
    totalR = 0
    
    rounds += 1
    
    #Operator Input Validity Checker
    while userInput.upper() not in "MDAS":
        
        userInput = input("Type the operation you would like to practice multiplication, division, addition, or subtraction? \n(M,D,A,S)\n" + "--->")
    
    inputStore1 = userInput.upper()
    
    gameInfo["Operator"] = inputStore1
    
    #Operator M or D Input Next Query
    if (inputStore1 == "M") or (inputStore1 == "D"):

        #User query on going upto or only practicing a number
        while userInput.upper() not in "UPTOONLY":
        
            userInput = input("Type ""Upto"" or ""Only"" to indicate whether you would like to practice upto a certain value or practice only that value.\n(Example: Going upto 12 includes multiplying 11's, 7's, etc. Whereas only 12 includes multiplying only 12's)\n--->")
        
        inputStore2 = userInput.upper()
        
        resetInputChecks()
        
        #In this case inputCheck is user to store whether or not the user's input is a number and that it is greater than 0, but less than 1000
        while (inputCheck[0] == False or inputCheck[1] == False or inputCheck[2] == False):
            
            if inputCheck[0] != True:
            
                if inputStore2 in "UPTO":
                    userInput = input("Enter a number you would like to practice up to\n(Example: 15 means going up to 15 x 15 or 225 / 15)\n--->")
                elif inputStore2 in "ONLY":
                    userInput = input("Enter a number you would like to practice\n(Example: 12 means only practicing multiples of 12)\n--->")
            
            if inputCheck[0] == True and inputCheck[1] != True and inputCheck[2] == True:
            
                if inputStore2 in "UPTO":
                    userInput = input("Enter a number other than 0 that you would like to practice up to\n(Example: 15 means going up to 15 x 15 or 225 / 15\n--->")
                elif inputStore2 in "ONLY":
                    userInput = input("Enter a number other than 0 that you would like to practice\n(Example: 12 means only practicing multiples of 12)\n--->")
                    
            if inputCheck[0] == True and inputCheck[1] == True and inputCheck[2] != True:
            
                if inputStore2 == "UPTO":
                    userInput = input("Enter a number less than or equal to 1000 that you would like to practice up to\n(Example: 15 means going up to 15 x 15 or 225 / 15\n--->")
                elif inputStore2 == "ONLY":
                    userInput = input("Enter a number less than or equal to 1000 that you would like to practice\n(Example: 12 means only practicing multiples of 12)\n--->")
            
            try:
                
                inputStore1 = int(userInput)
                
                resetInputChecks()
                
                if inputStore1 != 0 and inputStore1 <= 1000:
                    inputCheck[1] = True
                    inputCheck[2] = True
                    
                elif inputStore1 <= 1000:
                    
                    inputCheck[2] = True
                    
                elif inputStore1 != 0:
                    inputCheck[1] = True
                    
                
                inputCheck[0] = isinstance(inputStore1, int)
                
            except Exception as e:
                
                resetInputChecks()
                
                inputCheck[0] = isinstance(inputStore1, int)
            
        gameInfo["Number"] = inputStore1
        
        resetInputChecks()
        
        #If user chose to practice only one number query on second number else game List contains values going upto selected inital number
        if inputStore2 != "UPTO":
            
            while (inputCheck[0] == False or inputCheck[1] == False or inputCheck[2] == False):
                
                if inputCheck[0] == False:
                
                    userInput = input("Please type the second value you would like to go up to:\n(Example: 5 means we use the number you chose previously: " + str(gameInfo["Number"]) + " and we practice it up to 5 multiples. " + str(gameInfo["Number"]) + " x 5 or " + str(int(gameInfo["Number"]) * 5) + " / 5)\n--->")
                
                if inputCheck[0] == True and inputCheck[1] == False and inputCheck[2] == True:
                    
                    userInput = input("Enter a number other than 0 that you would like to practice up to\n(Example: 15 means going up to 15 x 15 or 225 / 15\n--->")
                
                if inputCheck[0] == True and inputCheck[1] == True and inputCheck[2] == False:
                    
                    userInput = input("Enter a number less than or equal to 1000 that you would like to practice up to\n(Example: 15 means going up to 15 x 15 or 225 / 15\n--->")
                
                try:
                
                    inputStore1 = int(userInput)
                
                    resetInputChecks()
                    
                
                    if inputStore1 != 0 and inputStore1 <= 1000:
                        inputCheck[1] = True
                        inputCheck[2] = True
                    
                    elif inputStore1 <= 1000:
                    
                        inputCheck[2] = True
                    
                    elif inputStore1 != 0:
                        inputCheck[1] = True
                
                    inputCheck[0] = isinstance(inputStore1, int)
                
                except Exception as e:
                    
                    resetInputChecks()
                
                    inputCheck[0] = isinstance(inputStore1, int)

            gameInfo["Up To Number"] = inputStore1
            
            gameList1 = int(gameInfo["Number"])

            for i in range(0,inputStore1):
                gameList2.append(i+1)
            
        else:
            
            for i in range(0,gameInfo["Number"]):
                gameList1.append(i+1)
        resetInputChecks()
        
    #Operator A or S Input Next Query
    elif (inputStore1 == "A") or (inputStore1 == "S"):
        
        userInput = "==="
        
        while userInput.upper() not in "ONESTENSHUNDREDS":
            
            userInput = input("Type Ones, Tens, or Hundreds to indicate what you would like to upto:\n(Example: Tens means 15 + 89 or 89 - 15)\n--->")
        
        gameInfo["Add/Sub Up To"] = userInput.upper()
    
        if userInput.upper() == "ONES":
            for i in range(len(myList)):
                if myList[i] < 10:
                    gameList1.append(myList[i])
    
        elif userInput.upper() == "TENS":
            for i in range(len(myList)):
                if myList[i] < 100:
                    gameList1.append(myList[i])

        elif userInput.upper() == "HUNDREDS":
            for i in range(len(myList)):
                if myList[i] < 1000:
                    gameList1.append(myList[i])
            
    else:
        print("Sorry the system has encountered an error. Please try again")
        
        break
    
    gameInfo["Number Limit Type"] = inputStore2
    
    roundGameInfo.append(gameInfo)
    
    #Query about timer
    while (userInput.upper() not in "YESNO"):
        userInput = input("Do you want a timer? (Yes/No)\n--->")

    #Checking timer input validity and following steps
    if (userInput.upper() == "YES"):
        
        resetInputChecks()
        
        while inputCheck[0] == False and inputCheck[1] == False:
            
            userInput = input("Enter time in seconds:\n--->")

            try:
                
                inputStore1 = int(userInput)
                
                inputCheck[0] = isinstance(inputStore1, int)
                
                if userInput == 0:
                    
                    resetInputChecks()
                    inputCheck[1] = False
                
            except ValueError:
                
                resetInputChecks()
                
                inputCheck[0] = isinstance(inputStore1, int)
    
        resetInputChecks()
    
        #Timer Setup
        timer = inputStore1
    
        seconds = timer % 60
        minutes = int(timer / 60) % 60
        hours = int(timer / 3600)
        print("The time you entered was : " + f"{hours:02}:{minutes:02}:{seconds:02}")
        
        timerList.append(str(hours) + ":" + str(minutes) + ":" + str(seconds))

        #Game Start
        while userInput.upper() not in "GO":
            userInput = input("Type ""Go"" to begin\n--->")
    
        #Timer Start
        for t in range(3, 0, -1):
            seconds = t % 60
            minutes = int(t / 60) % 60
            hours = int(t / 3600)
            print(f"{seconds:02}")
            time.sleep(1)

        timeStart = time.time()
    
    elif (userInput.upper() == "NO"):
        
        timerList.append("None")
        
        userInput = input("Type ""Go"" to begin\n--->")
        
        while userInput.upper() not in "GO":
            
            userInput = input("Type ""Go"" to begin\n--->")
        
        timer = 100000000000000000

    else:
        print("Sorry the system has encountered an error. Please try again")
        
        break
    
    timeStart = time.time()
    
    timeDiff = time.time() - timeStart

    #Game start
    
    while (userInput.upper() != "STOP") and (timeDiff < timer):
        
        streaksList.append(0)
        
        timeDiff = time.time() - timeStart
        
        length = 0
        ranNum1 = 0
        ranNum2 = 0
        
        if inputStore2 == "ONLY":
            
            length = len(gameList2)
            
            ranNum1 = random.randint(0, length-1)
            
        elif inputStore2 == "UPTO":
        
            length = len(gameList1)-1
            
            ranNum1 = random.randint(0, length-1)

            ranNum2 = random.randint(0, length-1)
        
        mode = gameInfo["Operator"]
        
        #Game Type Handlers
        
        if (mode == "M" and inputStore2 == "UPTO"):

            num1 = gameList1[ranNum1]

            num2 = gameList1[ranNum2]
        
            ans = num1*num2

            totalQ += 1

            userInput = input (str(num1) + " x " + str(num2) + " =       Score: " + str(score) + "   To stop type STOP\n--->")

            if userInput not in "STOPstopStop":

                try:
                    inputStore1 = int(userInput)
                    inputStore1 = "YES"
                except Exception as e:
                    inputStore1 = "NO"
            
                if inputStore1 == "YES" and int(userInput) == ans:

                    streak +=1

                    totalR +=1

                    if streak > 20:
                        score += 11
                    elif(streak > 15):
                        score += 7
                    elif(streak > 10):
                        score += 4
                    elif(streak > 5):
                        score += 2
                    else:
                        score += 1
                    
                    if streak > streaksList[rounds-1]:
                        
                        streaksList[rounds-1] = streak
                        
                    print("That's Right! Score: " + str(score) + "\n")

                else:
            
                    streak = 0

                    if score != 0:
                
                        score -=1
            
                    print("Incorrect. The answer was " + str(ans) + ".  Score: " + str(score) + "\n")

        elif (mode == "M" and inputStore2 == "ONLY"):
            
            num1 = int(gameInfo["Number"])
            
            num2 = gameList2[ranNum1]
            
            ans = num1*num2
            
            totalQ += 1

            userInput = input (str(num1) + " x " + str(num2) + " =       Score: " + str(score) + "   To stop type STOP\n--->")

            if userInput not in "STOPstopStop":

                try:
                    inputStore1 = int(userInput)
                    
                    inputStore1 = "YES"
                    
                except Exception as e:
                    inputStore1 = "NO"

            
                if inputStore1 == "YES" and int(userInput) == ans:

                    streak +=1

                    totalR +=1
                    

                    if streak > 20:
                        score += 11
                    elif(streak > 15):
                        score += 7
                    elif(streak > 10):
                        score += 4
                    elif(streak > 5):
                        score += 2
                    else:
                        score += 1
                    
                    if streak > streaksList[rounds-1]:
                        
                        streaksList[rounds-1] = streak
                        
                    print("That's Right! Score: " + str(score) + "\n")

                else:
            
                    streak = 0

                    if score != 0:
                
                        score -=1
            
                    print("Incorrect. The answer was " + str(ans) + ".  Score: " + str(score) + "\n")

        elif (mode == "D" and inputStore2 == "UPTO"):
            
            num1 = gameList1[ranNum1]

            num2 = gameList1[ranNum2]

            ans = num1 * num2

            totalQ += 1

            userInput = input (str(ans) + " / " + str(num1) + " =       Score: " + str(score) + "   To stop type STOP\n--->")
            
            if userInput not in "STOPstopStop":

                try:
                    inputStore1 = int(userInput)
                    
                    inputStore1 = "YES"
                    
                except Exception as e:
                    inputStore1 = "NO"

            
                if inputStore1 == "YES" and int(userInput) == num2:

                    streak +=1

                    totalR +=1
                    

                    if streak > 20:
                        score += 11
                    elif(streak > 15):
                        score += 7
                    elif(streak > 10):
                        score += 4
                    elif(streak > 5):
                        score += 2
                    else:
                        score += 1
                    
                    if streak > streaksList[rounds-1]:
                        
                        streaksList[rounds-1] = streak
                        
                    print("That's Right! Score: " + str(score) + "\n")

                else:
            
                    streak = 0

                    if score != 0:
                
                        score -=1
            
                    print("Incorrect. The answer was " + str(ans) + ".  Score: " + str(score) + "\n")


        elif (mode == "D" and inputStore2 == "ONLY"):
            
            num1 = int(gameInfo["Number"])

            num2 = gameList2[ranNum1]
            
            ans = num1 * num2

            totalQ += 1

            userInput = input (str(ans) + " / " + str(num1) + " =       Score: " + str(score) + "   To stop type STOP\n--->")
            
            if userInput not in "STOPstopStop":

                try:
                    inputStore1 = int(userInput)
                    
                    inputStore1 = "YES"
                    
                except Exception as e:
                    inputStore1 = "NO"

            
                if inputStore1 == "YES" and int(userInput) == num2:

                    streak +=1

                    totalR +=1
                    

                    if streak > 20:
                        score += 11
                    elif(streak > 15):
                        score += 7
                    elif(streak > 10):
                        score += 4
                    elif(streak > 5):
                        score += 2
                    else:
                        score += 1
                    
                    if streak > streaksList[rounds-1]:
                        
                        streaksList[rounds-1] = streak
                        
                    print("That's Right! Score: " + str(score) + "\n")

                else:
            
                    streak = 0

                    if score != 0:
                
                        score -=1
            
                    print("Incorrect. The answer was " + str(ans) + ".  Score: " + str(score) + "\n")

        elif (mode == "S"):
            
            length = len(gameList1)
            
            ranNum1 = random.randint(0, length-1)

            ranNum2 = random.randint(0, length-1)
        
            num1 = gameList1[ranNum1]

            num2 = gameList1[ranNum2]

            problem = ""

            if num1 > num2:
                
                problem = str(num1) + " - " + str(num2)
                ans = num1 - num2
            
            else:
                
                problem = str(num2) + " - " + str(num1)
                ans = num2 - num1

            totalQ += 1

            userInput = input (problem + " =       Score: " + str(score) + "   To stop type STOP\n--->")
            
            if userInput not in "STOPstopStop":

                try:
                    inputStore1 = int(userInput)
                    
                    inputStore1 = "YES"
                    
                except Exception as e:
                    inputStore1 = "NO"

            
                if inputStore1 == "YES" and int(userInput) == ans:
                
                    streak +=1

                    totalR += 1

                    if streak > streaksList[rounds-1]:
                        
                        streaksList[rounds-1] = streak

                    if streak > 20:
                        score += 11
                    elif(streak > 15):
                        score += 7
                    elif(streak > 10):
                        score += 4
                    elif(streak > 5):
                        score += 2
                    else:
                        score += 1

                    print("That's Right! Score: " + str(score) + "\n")

                else:
                
                    streak = 0

                    if score != 0:
                    
                        score -=1
                
                    print("Incorrect. The answer was " + str(ans) + ".  Score: " + str(score) + "\n")

        elif (mode == "A"):
            
            length = len(gameList1)
            
            ranNum1 = random.randint(0, length-1)

            ranNum2 = random.randint(0, length-1)
        
            num1 = gameList1[ranNum1]

            num2 = gameList1[ranNum2]

            ans = num1 + num2

            totalQ += 1

            userInput = input (str(num1) + " + " + str(num2) + " =       Score: " + str(score) + "   To stop type STOP\n--->")
            
            uInput = userInput.upper()

            if uInput != "STOP":
            
                try:
                    inputStore1 = int(userInput)
                    
                    inputStore1 = "YES"
                    
                except Exception as e:
                    inputStore1 = "NO"

            
                if inputStore1 == "YES" and int(userInput) == ans:
                
                    streak +=1

                    totalR += 1

                    if streak > streaksList[rounds-1]:
                        
                        streaksList[rounds-1] = streak

                    if streak > 20:
                        score += 11
                    elif(streak > 15):
                        score += 7
                    elif(streak > 10):
                        score += 4
                    elif(streak > 5):
                        score += 2
                    else:
                        score += 1

                    print("That's Right! Score: " + str(score) + "\n")

                else:
                
                    streak = 0

                    if score != 0:
                    
                        score -=1
                
                    print("Incorrect. The answer was " + str(ans) + ".  Score: " + str(score) + "\n")

        else:
            
            print("Sorry the system has encountered an error. Please try again")
        
            break

    if (timeDiff > timer):
        print("Times Up!")
    
    print("Your score is " + str(score) + "!" + " You got " + str(totalR) + " out of " + str(totalQ))
    
    scoreList.append(score)
    
    totalQList.append(totalQ)
    
    totalRList.append(totalR)
    
    roundGameInfo[rounds-1] = gameInfo.copy()
    
    while userInput.upper() not in "YESNO":
        
        userInput = input("Would you like to play again? (Yes/No)\n--->")
    
    inputStore1 = userInput.upper()
    
    if inputStore1 == "YES":
        
        playAgain = True
        
        inputStore1 = "---"
        
        while inputStore1 not in "YESNO":
            
            userInput = input("Would you like to see game statistics from all rounds?\n--->")
            
            inputStore1 = userInput.upper()
        
        if inputStore1 == "YES":
            
            print("Number of Rounds Played: " + str(rounds) + "\n")
            
            for i in range(rounds):
                
                print("Round " + str((i+1)) + ":")
                
                gameInfox = roundGameInfo[i]
                
                if (gameInfox["Operator"] == "M"):
                    
                    if (gameInfox["Number Limit Type"] == "ONLY"):
                        
                        print("Practiced multiplication for " + str(gameInfox["Number"]) + " up to " + str(gameInfox["Up To Number"]) + "!")
                    
                    else:
                        
                        print("Practiced multiplication up to " + str(gameInfox["Number"]) + "!")
                
                elif (gameInfox["Operator"] == "D"):

                        if (gameInfox["Number Limit Type"] == "ONLY"):
                        
                            print("Practiced division for multiples of " + str(gameInfox["Number"]) + " up to " + str(gameInfox["Up To Number"]) + "!")
                    
                        else:
                        
                            print("Practiced division up to multiples of " + str(gameInfox["Number"]) + "!")
                
                elif (gameInfox["Operator"] == "S"):
                    
                    print("Practiced subtraction with " + gameInfox["Add/Sub Up To"].lower() + "!")
                    
                elif (gameInfox["Operator"] == "A"):
                
                    print("Practiced addition with " + gameInfox["Add/Sub Up To"].lower() + "!")
                
                else:
                    print("Sorry the system has encountered an error. Please try again")
        
                
                print("Total Questions Given: " + str(totalQList[i]))
                
                print("Total Correct Responses Given: " + str(totalRList[i]))
                
                print("Highest Streak: " + str(streaksList[i]))
                
                print("Timer: " + str(timerList[i]))
                
                print("\n_____________________________________\n")
                
    elif inputStore1 == "NO":
        
        playAgain = False
        
        inputStore1 = "---"
        
        while inputStore1 not in "YESNO":
            
            userInput = input("Would you like to see game statistics from all rounds?\n--->")
            
            inputStore1 = userInput.upper()
        
        if inputStore1 == "YES":
            
            print("Number of Rounds Played: " + str(rounds) + "\n")
            
            for i in range(rounds):
                
                print("Round " + str((i+1)) + ":")
                
                gameInfox = roundGameInfo[i]
                
                if (gameInfox["Operator"] == "M"):
                    
                    if (gameInfox["Number Limit Type"] == "ONLY"):
                        
                        print("Practiced multiplication for " + str(gameInfox["Number"]) + " up to " + str(gameInfox["Up To Number"]) + "!")
                    
                    else:
                        
                        print("Practiced multiplication up to " + str(gameInfox["Number"]) + "!")
                
                elif (gameInfox["Operator"] == "D"):

                        if (gameInfox["Number Limit Type"] == "ONLY"):
                        
                            print("Practiced division for multiples of " + str(gameInfox["Number"]) + " up to " + str(gameInfox["Up To Number"]) + "!")
                    
                        else:
                        
                            print("Practiced division up to multiples of " + str(gameInfox["Number"]) + "!")
                
                elif (gameInfox["Operator"] == "S"):
                    
                    print("Practiced subtraction with " + gameInfox["Add/Sub Up To"].lower() + "!")
                    
                elif (gameInfox["Operator"] == "A"):
                
                    print("Practiced addition with " + gameInfox["Add/Sub Up To"].lower() + "!")
                
                else:
                    print("Sorry the system has encountered an error. Please try again")
        
                
                print("Total Questions Given: " + str(totalQList[i]))
                
                print("Total Correct Responses Given: " + str(totalRList[i]))
                
                print("Highest Streak: " + str(streaksList[i]))
                
                print("Timer: " + str(timerList[i]))
            
                print("\n_____________________________________\n")
                
        print("Thank You")
    