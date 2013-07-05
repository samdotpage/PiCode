from tkinter import* #imports tkinter
import random #imports random
import time, threading #imports time

tk = Tk() #creates 'tkapp' 
tk.title("Game") #makes window have title 'Game'
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
canvas=Canvas(tk,width=700, height=500, bd=0, highlightthickness=0) #defines the parameters of the canvas on which the game will be
canvas.grid(row = 1)
tk.update() #sends all information back to tkapp
root = Tk()

s = 3
ss = 3
x = 0
blobalob = 1
playAgain = 1

def add():
    global s
    s = s + 0.1
    global ss
    ss = ss + 0.09

def score():
    global x
    print (x)
    x = x + 1

def yes():
    playAgain = 1

def no():
    quit


class Ball: #creates the class ball

    
    def __init__(self, canvas, paddle, color): #initiates class
        self.canvas = canvas #brings previously defined canvas variable into class?
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25, fill=color) #makes the little red ball
        self.canvas.move(self.id, 245, 100)
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts) #makes it so you can use shuffle function on random
        self.x=starts[0] #random1zes the x axis value for the ball's spawn point 
        self.y=-3 # span point = -3 on y axis
        self.canvas_height=self.canvas.winfo_height() # makes it so it bounces off
        self.canvas_width=self.canvas.winfo_width()# the edges of the canvas
        self.hit_bottom = False            

    def draw(self):#effectively prints the ball onto the canvas
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y = s #SPEED
            add()
            score()
        if self.hit_paddle(pos) == True:
            self.y = -s
        if pos[3]>=self.canvas_height:
            self.hit_bottom = True
        if pos[0]<=0:
            self.x = s #SPEED
        if pos[2]>=self.canvas_width:
            self.x= -s

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False 

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 450)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, evt):
        self.x = -ss #SPEED

    def turn_right(self, evt):
        self.x = ss #SPEED

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red') # makes the little red ball red

while playAgain == 1:
    while 1:
        if ball.hit_bottom == False:
            ball.draw()
            paddle.draw()
        if ball.hit_bottom == True:
            scor = Label(text = "Well Done! You reached level " + str(x - 1) +"! Would you like to play again?", font = ('Calibri', 20))
            scor.grid(row = 8)
            no = Button(root, text = " NO ", command = no)
            no.grid(row = 4, column = 1)
        tk.update_idletasks()
        tk.update()
        time.sleep(0.001) #updates the balls atributes i.e. position, size etc. after every 0.01 seconds

root.mainloop()
