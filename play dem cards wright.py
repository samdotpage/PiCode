import random #import random module 
class Ting: #make a class for level objects 
    def __init__(self, maxx, Tingno): #when initializing, get cap and level no. 
        self.maxx = maxx 
        self.number = random.randint(0, maxx) #Get random number between 0 and cap
        self.level = Tingno 
    def check_number(self, x): #Make function to tell if guess is high or low 
        if x > self.number: 
            print ("That number is too high!") 
            return False #If the number is higher, return false 
        elif x < self.number: 
            print ("That number is too low!") 
            return False #if the number is lower, return false 
        else: 
            print ("That's it! YOU PASSED THE LEVEL" )
            return True #if the number is equal to the right one, return true       
ROUND1 = Ting(100, 1) 
ROUND2 = Ting(500, 2) 
FINALROUND = Ting(1000, 3) 
ROUNDS = [ROUND1, ROUND2, FINALROUND] 
x = 0 
currentlevel = ROUNDS[x] #set current level as level1 
print ("Welcome to Higher or Lower! Good Luck!" )
print ("Level", currentlevel.level, "\n\n") 
running = 1

while running: #While true 
    guess = input("Please guess a number between 0 and %d: "%currentlevel.maxx)
    guess=int(guess)
    if currentlevel.check_number(guess) == True: 
        x += 1 #bumps the index up for levels 
        if x >= len(ROUNDS): 
            print ("\n\n\n\n CONGRATS! YOU WIN THE GAME!") #If you win the last       level,  you win the game 
            running = 0 #game stops 
        else: 
            currentlevel = ROUNDS[x] #If not, go to the next level 
            print ("\n\nLevel", currentlevel.level, "\n\n") #Show current level 
