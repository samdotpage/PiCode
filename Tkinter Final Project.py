from tkinter import*#Open Tkinter
    
#Tell the user what to do
print("Try to click all the winning buttons")
print("Say what all the winnig buttons have in common")
print("When you think you know the pattern, close the buttons and take a guess!")
class App:#Create a class which opens the game

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()#Make the frame visible. From "Hello, again" of the Tkinter tutorial

        #Create a button sayong "First Python, then the world!!!" and causes you to lose
        row = 0#Make the row 0
        col = 0#Make the column 0
        self.world = Button(frame, text ="First Python, then the world!!!", fg="brown", bg="blue", command=self.loss)#Make the font colour brown
        self.world.pack()#Make the button visible

        #Create a button saying "Do you like eating apples?" and causes you to lose
        row = 0#Make the row 1
        col = 1#Make the column 0
        self.apples = Button(frame, text ="Do you like eating apples?", fg="orange", bg="green", command=self.loss)#Make the font colour orange
        self.apples.pack()#Make the button visible

        #Create a button saying "I like it when they sceam" and causes you to win
        row = 0#Make the row 0
        col = 2#Make the column 2
        self.scream = Button(frame, text ="I like it when they scream", fg="yellow", bg="brown", command=self.congratulate)#Make the font colour yellow
        self.scream.pack()#Make the button visible

        #Create a button saying "Example answer"
        row = 0#Make the row 0
        col = 12#Make the column 12
        self.example = Button(frame, text ="Example answer", fg="purple", bg="yellow", command=self.clue3)#Make the font colour pink
        self.example.pack()#Make the button visible
        
        #Create a button saying "Focus on the letters"
        row = 0#Make the row 0
        col = 3#Make the column 3
        self.help = Button(frame, text ="Extra Hint", fg="purple", bg="yellow", command=self.clue2)#Make the font colour purple
        self.help.pack()#Make the button visible
        
        #Create a button saying "Don't focus on the weaning"
        row = 0#Make the row 0
        col = 4#Make the column 4
        self.hint = Button(frame, text ="Hint", fg="purple", bg="yellow", command=self.clue1)#Make the font colour purple
        self.hint.pack()#Make the button visible
                           
        #Create a button saying "This will kill you" and causes you to win
        row = 0#Make the row 0
        col = 5#Make the column 5
        self.kill = Button(frame, text ="This will kill you", fg="blue", bg="pink", command=self.congratulate)#Make the font blue
        self.kill.pack()#Make the button visible

        #Create a button saying "Try to find the pattern" and causes you to lose
        row = 0#Make the row 0
        col = 6#Make the column 6
        self.pattern = Button(frame, text ="Try to find the pattern", fg="green", bg="red", command=self.loss)#Make the font green
        self.pattern.pack()#Make the button visible

        #Create a button saying "Click this to win" and causes you to win
        row = 0#Make the row 0
        col = 7#Make the column 7
        self.button = Button(frame, text="Click this to win", fg="red", bg="black", command=self.congratulate)#Make the font red
        self.button.pack()#Make the button visible
        
        #Create a button saying "Click this to lose" and causes you to lose
        row = 0#Make the row 0
        col = 8#Make the column 8
        self.win = Button(frame, text="Click this to lose", fg="turquoise", bg="purple", command=self.loss)
        self.win.pack()#Make the button visible

        #Create a button saying "I'm getting kind of bored" and causes you to win
        row = 0#Make the row 0
        col = 9#Make the column 9
        self.bored = Button(frame, text="I'm getting kind of bored", fg="PeachPuff", bg="SlateGrey", command=self.congratulate)#Make the font colour PeachPuff
        self.bored.pack()#Make the button visible

        #Create a button saying "Are you getting tired of this yet?" and causes you to win
        row = 0#Make the row 0
        col = 10#Make the column 10
        self.tired = Button(frame, text="Are you getting tired of this yet?", fg="dark salmon", bg="black", command=self.congratulate)#Make the font colour salmon brown
        self.tired.pack()#Make the button visible

        #Create a button saying "An apple a day keeps the doctor away" and causes you to lose
        row = 0#Make the row 0
        col = 11#Make the column 11
        self.doctor = Button(frame, text="An apple a day keeps the doctor away", fg="NavajoWhite2", bg="SlateGrey", command=self.loss)#Make the font colour NavajoWhite
        self.doctor.pack()#Make the button visible

        #Create a button saying "Straight back at you" and causes you to lose
        row = 0#Make the row 0
        col = 12#Make the column 12
        self.straight = Button(frame, text="Straight back at you", fg="red", bg="cyan", command=self.loss)#Make the font colour red
        self.straight.pack()#Make the button visible
        

    def loss(self):#Define self.loss
        print("You Lose")

    def clue3(self):#Define clue3
        print("If each winning button had 6 Zs, your answer would be zzzzzz")

    def clue2(self):#Define clue2
        print("Focus on the letters")

    def clue1(self):#Define clue1
        print("Don't focus on the meaning")
                        
    def congratulate(self):#define self.win
        print("You won!")

root = Tk()

app = App(root)#Creates an object 

root.mainloop()

def suggestion():
    guess = ''
    print("What is the answer?")#Ask the player to make a guess
    guess = input()
    if guess == 'iii':#If the guess is correcct:
        print("Congratulations! You did it!")#Congratulate the player
    else:#If the guess is not correct:
        print("That is not the correct answer. Do you want to guess again? (yes or no)")#Ask the player if he wants to try again
        if input() == 'yes':#If the player says yes:
            suggestion()#Reapeat the process
        else:
            print("I knew you'd give up eventually")
        
suggestion()#Call the function "Suggestion"
