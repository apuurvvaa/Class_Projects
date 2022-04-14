'''
develop a Python program to manage information about baseball players. The program will maintain the following information for each player in the data set:
player’s name (string) team identifier (string) games played (integer) at bats (integer)
runs scored (integer)
hits (integer)
doubles (integer)
triples (integer)
homeruns (integer) batting average (real) slugging percentage (real)
The first nine items will be taken from a data file; the last two items will be computed by the program. The following formulas will be used for those computations:
singles = hits - (doubles + triples + homeruns)
total bases = singles + 2*doubles + 3*triples + 4*homeruns batting average = (hits) / (at bats)
slugging percentage = (total bases) / (at bats)
A player with zero at bats is defined to have a batting average and slugging percentage of zero
2. The program will recognize the following commands:
QUIT
HELP
TEAM identifier
REPORT BATTINGAVERAGE REPORT SLUGGING PERCENTAGE
The program will recognize commands entered with any mix of upper and lower case letters.
The program will be operated interactively: it will prompt the user and accept commands from the keyboard.
If the user enters an invalid command, the program will display an appropriate message and prompt the user to enter another command.
3. The “QUIT” command will halt execution.
4. The "HELP" command will display information to the user about the commands recognized by the program.
5. The "TEAM" command will be followed by a string representing a team identifier. The program will display all information about all players on that team.
If the user enters an invalid team identifier, the program will display an appropriate message and prompt the user to enter another command;
6. The "REPORT" command will be followed by a string (BATTING" or "SLUGGING"). If the user enters an invalid command, the program will display an appropriate message and
prompt the user to enter another command; the program will not display an empty report.
If the user enters valid command “ REPORT BATTING”, generate a file named “ players_battingaverage.txt” that contains all the player information along with their batting average
IF the user enters valid command “ REPORT SLUGGING”, generate a file named “ players_sluggingpercentage.txt” that contains all the player information along with their slugging percentage.
7. The program will display appropriate messages to inform the user about any unusual circumstances.


'''


print("Choose from the following commands:\nQUIT \nHELP \nINPUT  \nTEAM  \nREPORT\n ")
  
f = open("Players.txt")
data = f.readline()
plist = []

while (data):
    data = data.strip().split(';')
    plist.append(data)
    data = f.readline()

# Make sure program runs through the different functions# Edit needs to be able to accept the TEAM command
def team(team_name = input("Enter Team Name:")):
    team_name = team_name.upper()
    for i in range(20):
        if team_name == plist[i][1].lstrip():
            print(plist[i])

def needs_help(a = input('Type HELP for assistance:')):
    while a == 'HELP':
   
        return print("Typing OUIT will end the program." + '\n'
        "Typing TEAM displays the information on all players on that team." + '\n'
        "Typing REPORT followed by BATTING or SLUGGING will display stats.")
needs_help()

def done(b = input('To end the Program, type QUIT: ')):
    b = 'QUIT'
    while b == 'QUIT':
            break
done()

def report_batting(rb = input('Type BATTING: ')):
    while rb == 'BATTING':
        batting_average = [plisti / plisti
        for plisti, plisti in zip(a, b) ]
        
        print(batting_average)
    if batting_average == 0:
        print("The player's batting average is 0.")
    else :
        bat_avg = open('players_battingaverage.txt', 'w')
report_batting()

def report_slugging(rs = input('Type SLUGGING: ')):
    while rs == 'SLUGGING':
        singles = hits - (doubles + triples + homeruns)
        total_bases = singles + 2 * doubles + 3 * triples + 4 * homeruns
        slugging_percentage = (total_bases) / (at_bats)# take this statement out, you won 't need it later
        print(slugging_percentage)
    if slugging_percentage == 0:
        print("The player's slugging percentage is 0.")
    else :
        slugging = open('players_sluggingpercentage.txt', 'w')
