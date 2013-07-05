from tkinter import* #imports tkinter
import random #imports random
import time #imports time

tk = Tk() #creates 'tkapp' 
tk.title("METEOR SHOWER!!") #makes window have title 'Game'
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
canvas=Canvas(tk,width=500, height=400,bg='cyan', bd=0, highlightthickness=0)  #defines the parameters of the canvas on which the game will be
canvas.pack() #packs canvas
tk.update()
E = ['red', 'purple', 'orange', 'yellow', 'brown']
x = 0

class Player:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,35,35, fill=color) # makes the shape,
        self.canvas.move(self.id, 200, 300) # you need to edit this
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

class Meteor: #creates the class ball
    def __init__(self, canvas, player, color): #initiates class
        b = random.randint(25, 60)
        self.canvas = canvas #brings previously defined canvas variable into class?
        self.player = player
        self.id = canvas.create_oval(10,10,b,b, fill=color) #makes the little red ball
        self.canvas.move(self.id, random.randint(20, 380), 0)
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts) #makes it so you can use shuffle function on random
        self.x=random.uniform(-0.5, 0.5)  #random1zes the x axis value for the ball's spawn point 
        self.y=-3 # span point = -3 on y axis
        self.canvas_height=self.canvas.winfo_height() # makes it so it bounces off
        self.canvas_width=self.canvas.winfo_width()# the edges of the canvas
        self.hit_bottom = False

    def draw(self):
        global x#effectively prints the ball onto the canvas
        e = random.uniform(2.5, 4.5)
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=e #speed for
        if self.hit_player(pos) == True:
            self.hit_bottom = True
            w = Label(text = ('Well done, you dodged ' + str(x) + ' meteors!'), font = ('Calibri', 20), bg = ('green'), width = (35))
            w.pack()
        if pos[3]>=self.canvas_height:
            self.__init__(canvas, player, E[random.randint(0, 4)])
            x = x + 1
        if pos[0]<=0:
                self.x=e
        if pos[2]>=self.canvas_width:
                self.x=-e

    def hit_player(self, pos):
        player_pos = self.canvas.coords(self.player.id)
        if pos[2] >= player_pos[0] and pos[0] <= player_pos[2]:
            if pos[3] >= player_pos[1] and pos[3] <= player_pos[3]:
                return True
        return False

class FLOOR:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.meteor = meteor
        self.id=canvas.create_rectangle(1000,1000,0,0,fill=color)
        self.canvas.move(self.id,-100,350)
        self.canvas_width=self.canvas.winfo_width()

    def draw(self):
        pos = self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=0
        elif pos[2] >=self.canvas_width:
            self.x=0
    
player = Player(canvas, 'black')
meteor = Meteor(canvas, player, 'red')
meteor2 = Meteor(canvas, player, 'orange')
meteor3 = Meteor(canvas, player, 'yellow')
meteor4 = Meteor(canvas, player, 'purple')
ground = FLOOR(canvas, 'green')

while 1:
    if meteor.hit_bottom == False and meteor2.hit_bottom == False and meteor3.hit_bottom == False and meteor4.hit_bottom == False:
        ground.draw()
        meteor.draw()
        meteor2.draw()
        meteor3.draw()
        meteor4.draw()
        player.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
