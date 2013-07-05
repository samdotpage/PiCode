from tkinter import *
import random
import time
p1score = 0
p2score = 0

tk = Tk()#makes all the Tk ever
tk.title("Game")#name of the thingmabobcake window as Game
tk.resizable(0, 0)#makes it resizable?
tk.wm_attributes("-topmost",1)#?
canvas = Canvas(tk, width=500, height=800, bd=0, highlightthickness=0)#makes the actual canvas
canvas.grid(row = 1, column = 1)#packs the canvas like a nice packed lunch
tk.update()#updates?


class Ball:
    def __init__ (self, canvas, paddle, paddleb, color):
        self.canvas = canvas #makes a nice mummy canvas for the the ball
        self.paddle = paddle
        self.paddleb = paddleb
        self.id = canvas.create_oval(0,400,15,415, fill=color) #defines the making of the ball in the canvas
        self.canvas.move(self.id, 245, 100) #defines the moviness of the ball? Doesn't do anything atm
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -4
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.hit_top = False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.hit_top = True
            self.y = 4
        if self.hit_paddle(pos) == True:
            self.y = -4
        if self.hit_paddleb(pos) == True:
            self.y = 4 
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            self.y = -4
        if pos[0] <= 0:
            self.x = 4
        if pos[2] >= self.canvas_width:
            self.x = -4

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        self.hit_paddlea_cats = False
        if pos[2] >= paddle_pos[0]  and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        self.hit_paddlea_cats = True
        return False
    
    def hit_paddleb(self, pos):
        self.hit_paddleb_cats = False
        paddleb_pos = self.canvas.coords(self.paddleb.id)
        if pos[2] >= paddleb_pos[0]  and pos[0] <= paddleb_pos[2]:
            if pos[1] <= paddleb_pos[3] and pos[1] >= paddleb_pos[1]:
                return True
        self.hit_paddleb_cats = True
        return False
    
class Paddle:
    def __init__(self, canvas, color, player):
        self.canvas = canvas
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        if player == 1:
            self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
            self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
            self.id = canvas.create_rectangle(0, 390, 100, 400, fill=color)
            self.canvas.move(self.id, 200, 300)
        if player == 2:
            self.canvas.bind_all('<KeyPress-a>', self.turn_left)
            self.canvas.bind_all('<KeyPress-d>', self.turn_right)
            self.id = canvas.create_rectangle(0, -190, 100, -200, fill=color)
            self.canvas.move(self.id, 200, 300)

    def turn_left(self, evt):
        self.x = -3
    def turn_right(self, evt):
        self.x = 3

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <=0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
            
paddle = Paddle(canvas, 'blue', 1)
paddleb = Paddle(canvas, 'green', 2)
ball = Ball(canvas, paddle, paddleb, 'red')#*should* make a ball which is an instance of a ball class
while 1:  
    ball.draw()
    paddle.draw()
    paddleb.draw()

    if ball.hit_bottom == True:
        p2score = p2score + 1
        ball.hit_bottom = False
        scoreboard = Label(text = '     ''P1 Score (bottom): ' + str(p1score) + ' P2 Score (top): ' + str(p2score) + '       ').grid(column = 1, row = 2)
    if ball.hit_top == True:
        p1score = p1score + 1
        ball.hit_top = False
        scoreboard = Label(text = '     ''P1 Score (bottom): ' + str(p1score) + ' P2 Score (top): ' + str(p2score) + '       ').grid(column = 1, row = 2)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.001)#updates the location of stuff and more stuff like the ball every 0.01secs


