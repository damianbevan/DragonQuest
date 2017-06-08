import random
import time

####################
# Global Variables #
####################

# Sleep Time
sleepTime = 2
# Doors
maxNumberOfDoors = 10
minNumberOfDoors = 5
# Gold
maxGold = 100
minGold = 1
totalGold = 0

#################
### Functions ###
#################

# Welcome the player
def welcome():
    print ("Welcome to Dragon Quest!!!\n")
    sleep()

# Choose the cave to enter
def chooseCave( numberOfDoors ):

    if ( 0 == totalGold ):
        print ("You enter a large cave...")
        sleep()
        print ("It is dark and scary...")
        sleep()     
        print ("You can see " + str( numberOfDoors ) + " wooden doors ahead.")
        sleep()
        print ("One leads to certain death and the others to wealth and riches!")
    else:
        print ("You stumble on in the dark and see " + str( numberOfDoors ) + " more doors ahead" )
    sleep()
    caveNumber = '0'
    while ( int( caveNumber ) < 1 or int( caveNumber ) > int(numberOfDoors )):
        print ("Which door number would you like to go through? ", end='')
        caveNumber = inputInt()
        
    return caveNumber

# Enter the cave
def enterCave( numberOfDoors, doorNumber ):
    randomNumber = random.randint( 1, numberOfDoors )
    treasure = 0
    
    print ( 'You enter door ' + doorNumber + " and see a large fierce fire breathing dragon...")
    sleep()
    print ( 'He opens his jaws and...' )
    sleep()
    # If user enters the same cave number as the random number then they lose
    if  ( int( doorNumber ) == randomNumber ):
        print ('Eats you alive!!!!')
    else:
        treasure = random.randint( minGold, maxGold )
        print ('Gives you ' + str( treasure ) + ' gold coins!')
    sleep()
    return treasure

# Calculate the cave of death
def calculateDoors():
    doors = random.randint( minNumberOfDoors, maxNumberOfDoors )
    return doors
    
# Sleep for a set period of time
def sleep():
    time.sleep( sleepTime )

# Get a valid integer input
def inputInt():
    stringInt = ""
    validInt = False
    while ( False == validInt ):
        stringInt = input()
        validInt = stringInt.isnumeric()
        if ( validInt == False ):
            print ("Please enter a number: ", end= '');
    return stringInt

################
# Main Program #
################
playAgain = 'y'
numberOfDoors = 0

# Welcome the player
welcome()
    
while ( playAgain == 'y' or playAgain == 'Y' ):

    numberOfDoors = calculateDoors()
    
    # Ask for cave number
    caveNumber = chooseCave( numberOfDoors )

    # Process caveNumber
    treasureInCave = enterCave( numberOfDoors, caveNumber )

    # Calculate gold
    if ( treasureInCave > 0 ):
        totalGold = totalGold + treasureInCave
    else:
        totalGold = 0

    if ( totalGold > 0 ):
        print ("You now have " + str( totalGold ) + " gold coins")
        print ( "Would you like to continue on?", end='')
    else:
        print ("You died and have no gold!")
        print ( "Would you like to start again?", end='')
              
    print ("(y)es or (n)o?")
    
    playAgain = input()

if ( totalGold > 0 ):
    print( "Congratulations you made it out alive with " + str(totalGold) + " gold coins!")
else:
    print( "Bad luck, you left with no gold." )
