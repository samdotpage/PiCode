from tkinter import *
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

class Ball:
    def __init__(self, canvas, paddle, paddle2, color):
        self.canvas = canvas
        self.paddle = paddle
        self.paddle2= paddle2
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = starts[0]
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.hit_top=False 
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if self.hit_paddle(pos) == True:
            self.y = -3
        if self.hit_paddle2(pos) == True:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if pos[3]<=self.canvas_height:
            self.hit_top=True
        if pos[0] <= 0:
            self.x =3
        if pos[2] >= self.canvas_width:
            self.x = -3
            
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def hit_paddle2(self,pos):
        paddle2_pos = self.canvas.coords(self.paddle2.id)
        if pos[2] >= paddle2_pos[0] and pos[0] <= paddle2_pos[2]:
            if pos[3] >= paddle2_pos[1] and pos[3] <= paddle2_pos[3]:
                return True
        return False

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 300, 380)
        self.x = 0
        self.y=0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Up>', self.move_up)
        self.canvas.bind_all('<KeyPress-Down>', self.move_down)
        
    def turn_left(self, evt):
        self.x = -2
        
    def turn_right(self, evt):
        self.x = 2

    def move_up(self,evt):
        self.y=-2
    def move_down(self,evt):
        self.y=2
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
            self.y=0
        elif pos[2] >= self.canvas_width:
            self.x = 0
            self.y=0

class Paddlee:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 300, 20)
        self.x = 0
        self.y=0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-a>', self.turn_left)
        self.canvas.bind_all('<KeyPress-d>', self.turn_right)
        self.canvas.bind_all('<KeyPress-w>', self.move_up)
        self.canvas.bind_all('<KeyPress-s>', self.move_down)
        
    def turn_left(self, evt):
        self.x = -2
        
    def turn_right(self, evt):
        self.x = 2

    def move_up(self,evt):
        self.y=-2
    def move_down(self,evt):
        self.y=2
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
            self.y=0
        elif pos[2] >= self.canvas_width:
            self.x = 0
            self.y=0
     
paddle = Paddle(canvas, 'blue')
paddle2 = Paddlee(canvas,'red')
ball = Ball(canvas, paddle, paddle2, 'red')
ball2 = Ball(canvas, paddle, paddle2, 'cyan')
ball3 = Ball(canvas, paddle, paddle2, 'green')
ball4 = Ball(canvas, paddle, paddle2, 'yellow')


while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
        ball2.draw()
        paddle2.draw()
        ball3.draw()
        ball4.draw()
    if ball2.hit_bottom == False:
        ball.draw()
        paddle.draw()
        ball2.draw()
        paddle2.draw()
        ball3.draw()
        ball4.draw()
    if ball3.hit_bottom == False:
        ball.draw()
        paddle.draw()
        ball2.draw()
        paddle2.draw()
        ball3.draw()
        ball4.draw()
    if ball4.hit_bottom == False:
        ball.draw()
        paddle.draw()
        ball2.draw()
        paddle2.draw()
        ball3.draw()
        ball4.draw()
    if ball.hit_top == False:
        ball.draw()
        paddle.draw()
        ball2.draw()
        paddle2.draw()
        ball3.draw()
        ball4.draw()
    if ball2.hit_top == False:
        ball.draw()
        paddle.draw()
        ball2.draw()
        paddle2.draw()
        ball3.draw()
        ball4.draw()
    if ball3.hit_top == False:
        ball.draw()
        paddle.draw()
        ball2.draw()
        paddle2.draw()
        ball3.draw()
        ball4.draw()
    if ball4.hit_top == False:
        ball.draw()
        paddle.draw()
        ball2.draw()
        paddle2.draw()
        ball3.draw()
        ball4.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.08)

