'''

This assignment focuses on the design and implementation of Python programs to process data files (File I/O) using compound objects such as dictionaries, tuples, lists and sets.
Description:

1. In this project you will develop a Python program to manage information about baseball players.  The program will maintain the following information for each player in the data set:

player’s name (string)
team identifier (string)
games played (integer)
at bats (integer)
runs scored (integer)
hits (integer)
doubles (integer)
triples (integer)
homeruns (integer)
 
2.  The program will recognize the following commands:

QUIT
HELP
INPUT file_path
TEAM identifier
REPORT n HITS

The program will recognize commands entered with any mix of upper and lower case letters. The program will be operated interactively:  it will prompt the user and accept commands from the keyboard. Your program should show the following prompt to accept commands.

Please enter a command (HELP to list acceptable commands):

If the user enters an invalid command, the program will display an appropriate message and prompt the user to enter the next command.

3.  The “QUIT” command will halt execution.

4.  The "HELP" command will display information to the user about the commands recognized by the program.

5.  The "INPUT" command will be followed by a string representing the path/name of an input file.  The program will discard the current data set stored in memory, and then process the input file as the source for a new data set (open the file, read the file once and store the records in a compound structure, then close the file).

An input file contains zero or more player records, where each record consists of the nine fields listed above.  The records are separated by newlines, and the fields are separated by semicolons.

If the user enters an invalid file name, the program will display an appropriate message and prompt the user to enter the next command.

6.  The "TEAM" command will be followed by a string representing a team identifier.  The program will display all information about all players on that team, in alphabetical order.

The information will be displayed in tabular form.  The fields will be identified using column headers, and the fields will be aligned beneath the headers.

If the user enters an invalid team identifier, the program will display an appropriate message and prompt the user to enter the next command; the program will not display an empty table.

 
7.  The "REPORT" command will be followed by an integer number and a string ("HITS").

If the user enters an invalid command, the program will display an appropriate message and prompt the user to enter the next command; the program will not display an empty report.

For the report, the program will display all information about the top "n" players with highest HITS:

The report will be sorted from highest to lowest value in the category.  Players with the same number of hits will be displayed in alphabetical order.

The information will be displayed in tabular form.  The fields will be identified using column headers, and the fields will be aligned beneath the headers.  Any floating point value will be displayed with three digits of precision following the decimal point.

8.  The program will display appropriate messages to inform the user about any unusual circumstances.

9.  The program will consist of at least four meaningful functions.  Communication between functions will occur via parameters and return values; you may not use any global variables.

Reminders:

1.  The file named “mlb.2013.txt” contains information about players on the teams in Major League Baseball in 2013.

2.  The file named “mlb.part.txt” contains information about 20 players on teams in Major League Baseball in 2013; that file will be useful for your initial development.  The first few lines of that file are shown below:

De Aza, Alejandro; CWS; 153; 607; 84; 160; 27; 4; 17
Hunter, Torii; DET; 144; 606; 90; 184; 37; 5; 17
Hamilton, Josh; LAA; 151; 576; 73; 144; 32; 5; 21
Choo, Shin-Soo; CIN; 154; 569; 107; 162; 34; 2; 21
Upton, Justin; ATL; 149; 558; 94; 147; 27; 2; 27
Cabrera, Miguel; DET; 148; 555; 103; 193; 26; 1; 44
Posey, Buster; SF; 148; 520; 61; 153; 34; 1; 15
Suzuki, Ichiro; NYY; 150; 520; 57; 136; 15; 3; 7
Holliday, Matt; STL; 141; 520; 103; 156; 31; 1; 22
Headley, Chase; SD; 141; 520; 59; 130; 35; 2; 13
 
3.  As noted above, your program must consist of at least four meaningful functions; you certainly may develop more than four functions.  You will have to decide how to decompose the overall program into smaller tasks.  Note that it would be natural to implement some (or even all) of the subtasks as functions. Naturally, you may have at least one function for each acceptable command. Additionally, you may have another function checking the validity of a user-entered command.

Each function must be declared at the global level.  Each function should have a coherent purpose which can be expressed succinctly in a line or two.

You may not use any global variables in your program.  All communication between the functions which constitute your program will be done using parameters and return values.

4. Develop a simple version of the program, then add functionality incrementally, testing your program thoroughly after each addition.

5.  Note that you must sort the data set (your list of tuples) to prepare the various reports.  There are a number of different strategies that you could use, including:

Develop your own sorting function
Use the built-in function sorted
Use the list method sort

There is a nice introduction to sorting on the Python website:

	https://wiki.python.org/moin/HowTo/Sorting#Sorting_Mini-HOW_TO

Please note the use of function “itemgetter” in the section on “Operator Module Functions”.

Deliverables:

A Python file named “Baseball_CLID.py" with the implementation of the program defined above. The  file should have your name and CLID at the beginning as two comment lines.
A pdf file named "Report_CLID.pdf". You do not need to provide a detailed report. Your report should contain one sentence for each item in the “Description” section explaining whether you were able to implement the task or not.

Notes:

Your program should be user friendly and prompt the user whenever it requires his/her interaction (e.g., asking him/her to enter a value).
	· Your source code should conform to common practices in terms of variable names, indentation, comments, and so on.
	· Variable/Method names should start with lower case, if it has multiple words each word after the first one should be capital and the entire name should be one word
	· Put line comments before for/while loops and briefly tell what they do
	· In case you have if/else blocks that are longer than two lines of code put a line comment into the block at the beginning and briefly explain what the condition is and what is carried out
	· Follow the indentation rules that I follow in the class while writing code

'''

print("Welcome to The Baseball Database!")

def terminate():
    """This function quits the program"""
    userExit = input("Are you sure you want to quit? Yes or No?: ")
    userExit = userExit.lower()
    if userExit == "yes":
        print("The Baseball Database is terminating gracefully.")
        exit()
    if userExit == "no":
        introRerun()
    else:
        print("Please enter 'Yes' or 'No'.")
        terminate()

def assist():
    """This function offers help to the user"""
    print("The Baseball Database supports the following command functions:")
    print("INPUT - which allows you to input a file path")
    print("TEAM - which allows you to identify a team, and provide info about the players")
    print("REPORT - which reports the number of hits")
    print("HELP - for assistance")
    print("QUIT - to exit the database")
    print("Please choose from one of the above functions.")
    introRerun()


def filePath():
    """This function allows the user to input a file"""
    file = input("Please enter the file path to read: ")
    fileObject = open(file) 
    return fileObject

#def teamInfo():
#    print(fileObject)
#    introRerun()

def introRerun():
    """This function reprompts the user to enter a command"""
    introLoop = input("Please enter a command, or type 'Help' for a list of options: ")
    introLoop = introLoop.lower()
    if introLoop == "quit":
        terminate()
        
    if introLoop == "help":
        assist()
    
    if introLoop == "input":
        filePath()
        
    if introLoop == "team":
        processFile(fileObject)
        
    else:
        print("Please enter a valid command, for a list of options type 'Help'")
        introRerun()
        

def processFile(fileObject):
    """This function processes the input file"""
    myList = []
    fileHandle = (fileObject, "r")
    for line in fileHandle:
        tokens = line.split(sep = ";")
        entry = {"Name" : tokens [0], "Team" : tokens [1], "Games Played" : tokens [2], "At Bats" : tokens [3], "Runs Scored" : tokens [4], "Hits" : tokens [5], "Doubles" : tokens [6], "Triples" : tokens [7], "Homeruns" : tokens [8]}
        myList.append(entry)
    return myList


playerList = None

intro = input("Please enter a command, or type 'Help' for a list of options: ")
intro = intro.lower()

if intro == "help":
    assist()
if intro == "input":
    filePath()
    fileObject = filePath()
    introRerun()
if intro == "team":
    if playerList != None:
        print("Error! You must first INPUT a file to be read!")
        filePath()
    else:
        filePath()
if intro == "no" or intro == "quit":
    terminate()
    
#playerList = None
#processFile = fileObject
#playerList = processFile(filePath)
#if command == "team":
#    if playerList != None:
#        print("Error! You must first INPUT a file to be read!")
#        filePath()
#else:
#    filePath()
    
#userFile = input("Would you like to input a file? Yes or No?: ")
#userFile = userFile.lower()
#if userFile == "yes":
#    fileObject = fileInput()
#    fileObject = open(fileObject, "r")
#if userFile == "no":
#    introRerun()
    
#else:
#    terminate()
    

#userHelp = input("Would you like any assistance in navigating The Baseball Database? Yes or No?: ")
#userHelp = userHelp.lower()
#if userHelp == "yes" or userHelp == "help":
#    assist()
#else:
#    intro

                                  
#userExit = input("Would you like to continue? Yes or No?: ")
#userExit = userExit.lower()
#if userExit == "yes":
#    terminate()
#else:
#    intro


#def Quit(commandQuit):
#        yes = True
#        if commandQuit == True:
#            print("Program terminating gracefully")
#        else:
#            input("Please enter a command:")
#            return 
                  
    
#yesExit = input("Would you like to continue?:").lower()
#Quit(yesExit) 
##### how to use .lower()









