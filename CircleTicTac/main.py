# Circular Tic-Tac-Toe
# Written By: Kanwarpal, JustColdToast
# Build version: v1.1  Date: 22/03/2019
# Latest additions: Screen scaling for board size
# Planned additions: Fixed board-clear function

import turtle
class Main():
    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.setup(width = 1.0, height = 1.0)
        self.wn.title("Circular Tic-Tac-Toe v1.2")
        self.wn.bgcolor("#6a6d72")
        screen = self.wn.getcanvas()
        self.t = turtle.Turtle()
        self.x = self.wn.window_width()/2
        self.y = self.wn.window_height()/2
        self.t.pensize(2)
        # formats the scaling of the grid in reference to the 1080p screen
        self.heightRatio = self.wn.window_height() / 1080
        self.t.speed(0)
        self.t.pencolor("white")
        screen.bind('<Motion>', self.set_coords)  # Bind for setting the coordinates of the turtle
        screen.bind('x', self.draw_x)
        screen.bind('o', self.draw_o)
        self.draw_board()
        #self.run()
    def draw_board(self):  # Function to draw the game board
        # Below are the base points used on the circle, multiplied the the change of screen size
        # (80,0), (56,56), (0,80), (-56,56), (-80, 0), (-56, -56), (0, -80), (56,-56)
        circlepoints = [(int(80*self.heightRatio), 0),
                        (int(56*self.heightRatio), int(56*self.heightRatio)),
                        (0, int(80*self.heightRatio)),
                        (-1*int(56*self.heightRatio), int(56*self.heightRatio)),
                        (-1*int(80*self.heightRatio), 0),
                        (-1*int(56*self.heightRatio), -1*int(56*self.heightRatio)),
                        (0, -1*int(80*self.heightRatio)),
                        (int(56*self.heightRatio), -1*int(56*self.heightRatio))]
        self.t.speed(0)
        self.t.clear()
        self.t.penup()
        self.t.goto(0, 0)
        for pos in range(0, int(80*self.heightRatio)*6, int(80*self.heightRatio)):
            if pos == int(80*self.heightRatio):
                self.t.fillcolor("white")
                self.t.penup()
                self.t.goto(0,0-pos)
                self.t.begin_fill()
                self.t.circle(pos)
                self.t.end_fill()
            self.t.penup()
            self.t.goto(0, 0 - pos)
            self.t.pendown()
            self.t.circle(pos)
        # Belows draws grid lines outwards from center
        for i in range(0, len(circlepoints)):
            self.t.penup()
            self.t.goto(circlepoints[i][0], circlepoints[i][1])
            self.t.seth(0+(45*i))
            self.t.pendown()
            self.t.fd(int(320*self.heightRatio))
        # Redundant method for drawing the game board, compatible only with 1080p screen; legacy use
        '''  
        self.t.penup()
        self.t.goto(0, 80)
        self.t.seth(90)
        self.t.pendown()
        self.t.fd(320)
        self.t.penup()
        self.t.goto(80,0)
        self.t.pendown()
        self.t.seth(0)
        self.t.fd(320)
        self.t.penup()
        self.t.goto(56, 56)
        self.t.seth(45)
        self.t.pendown()
        self.t.fd(320)
        self.t.penup()
        self.t.goto(-80,0)
        self.t.seth(180)
        self.t.pendown()
        self.t.fd(320)
        self.t.penup()
        self.t.goto(0,-80)
        self.t.seth(270)
        self.t.pendown()
        self.t.fd(320)
        self.t.penup()
        self.t.goto(-56,56)
        self.t.seth(135)
        self.t.pendown()
        self.t.fd(320)
        self.t.penup()
        self.t.goto(-56,-56)
        self.t.seth(225)
        self.t.pendown()
        self.t.fd(320)
        self.t.penup()
        self.t.goto(56,-56)
        self.t.seth(315)
        self.t.pendown()
        self.t.fd(320)
        self.t.penup()
        '''
        self.t.speed(10)
        self.t.penup()  # Lifts the art.t back up, to prevent further drawing
    def draw_x(self):
        self.run()
        self.t.pendown()
        self.t.seth(45)
        self.t.forward(int(25*self.heightRatio))
        self.t.seth(225)
        self.t.forward(int(50*self.heightRatio))
        self.t.seth(45)
        self.t.forward(int(25*self.heightRatio))
        self.t.seth(135)
        self.t.forward(int(25*self.heightRatio))
        self.t.seth(315)
        self.t.forward(int(50*self.heightRatio))
        self.t.penup()
    def draw_o(self):
        self.run()
        self.t.penup()
        self.t.sety(self.t.ycor()-int(25*self.heightRatio))
        self.t.setx(self.t.xcor()-int(13*self.heightRatio))
        self.t.pendown()
        self.t.circle(int(25*self.heightRatio))
        self.t.penup()
    def set_coords(self, event):
        self.x = event.x
        self.y = event.y
    def run(self):
        self.t.penup()
        self.t.setposition(self.x-self.wn.window_width()/2, (self.y*-1)+self.wn.window_height()/2)
            
art = Main()  # Object of main class, representing the turtle

art.wn.onkey(art.draw_x, 'x')
art.wn.onkey(art.draw_o, 'o')
art.wn.onkey(art.draw_board, 'g')
art.wn.listen()
art.t.showturtle()
art.wn.mainloop()
