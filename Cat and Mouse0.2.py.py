#Collaborative Project#
#13/03/13#
#Version 0.1 preAlpha#
#Last Editor: Edward#


#Modules#
from tikiner import *
import random
import time


#Classes#
class App:

    def __init__(self,button,label):
        self.button = Button(text="Quit", command=quit)
        self.button.grid(row=1, column = 1)

        self.A = label(text = "1")
        self.A.grid(row=2, column=2)

        self.B = label(text = "2")
        self.B.grid(row=2, column=3)

        self.C = label(text = "3")
        self.C.grid(row=2, column=4)

        self.D = label(text = "4")
        self.D.grid(row=3, column=2)

        self.E = label(text = "5")
        self.E.grid(row=3, column=3)

        self.F = label(text = "6")
        self.F.grid(row=3, column=4)

        self.G = label(text = "7")
        self.G.grid(row=4, column=2)
        
        self.H = label(text = "8")
        self.H.grid(row=4, column=3)

        self.I = label(text = "9")
        self.I.grid(row=4, column=4)
        



#Functions#

def playAgain():
    print('Play Again? (y/n)')
    return input()


#Program Start#


running = 'y'

while running = 'y':
    root= Tk()
    app=App(root)
    root.mainloop
    
