
import turtle
import random
import math

COL = (0.078431373, 0.117647059,0.490196078) #start color RGB: 20, 30, 125
TAR = (0.968627451, 0.270588235, 0.376470588) #target color RGB: 247, 69, 96
WID, HEIG = 600, 600

screen = turtle.Screen()
turtle = turtle.Turtle()
turtle.speed(0)

def draw_background(COL, TAR, WID, HEIG):#doing background with a color gradient
    
    delt = [(red - COL[index]) / HEIG for index, red in enumerate(TAR)]
    turtle.color(COL)
    turtle.penup()
    turtle.goto(-WID/2, HEIG/2)
    turtle.pendown()
    direction = 1

    for distance, y in enumerate(range(HEIG//2, -HEIG//2, -1)):

        turtle.forward(WID * direction)
        turtle.color([COL[i] + delta * distance for i, delta in enumerate(delt)])
        turtle.sety(y)

        direction *= -1

def draw_sun(WID): #doing sun, that is located in the middle of the picture
    turtle.color('gold')
    turtle.penup()
    turtle.goto(100, 0)
    turtle.pendown()
    turtle.left(90)
    turtle.fillcolor('gold')
    turtle.begin_fill()
    turtle.circle(WID/6)
    turtle.end_fill()

    for _ in range(8):#doing arms for the sun
        turtle.pensize(7)
        turtle.penup()
        turtle.goto(0,0)
        turtle.left(45)
        turtle.forward(120)
        turtle.pendown()
        turtle.forward(50)


def draw_wave(x, y, n, radius_up, radius_down, color): #doing general wave code, where the radius, color and position can be set
    turtle.color(color) 
    turtle.pensize(5) 
    turtle.penup() 
    turtle.goto(300, y) 
    turtle.pendown()
    turtle.begin_fill()

    for _ in range(n):
        turtle.circle(radius_up, 180)
        turtle.left(180)
        turtle.circle(radius_down, -180)
        turtle.left(180)
    
    turtle.left(180)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(600)
    turtle.left(90)
    turtle.forward(x)
    turtle.end_fill()

def draw_waves():#doing diffrent waves
    draw_wave(60, 0, 6, 20, 30, 'darkblue') # n = 600 /((2*radius1)+(2*radius2))
    draw_wave(50, -35, 5, 35, 25, 'navy')
    draw_wave(50, -50, 10, 15, 15, 'blue4')
    draw_wave(50, -80, 6, 35, 15, 'blue3')
    draw_wave(50, -105, 12, 10, 15, 'blue2')
    draw_wave(50, -135, 6, 30, 20, 'blue')
    draw_wave(70, -155, 10, 15, 15, 'darkslateblue')
    draw_wave(50, -185, 6, 20, 30, 'cornflowerblue')
    draw_wave(50, -215, 10, 20, 10, 'deepskyblue')
    draw_wave(50, -235, 5, 25, 35, 'skyblue')
    draw_wave(40, -260, 10, 15, 15, 'cyan')
    draw_wave(10, -290, 10, 25, 5, 'aquamarine')

def draw_fish(n): #doing fishs, that have diffrent sizes, positions and colors
    colors = ['lavenderblush', 'indianred', 'lightsalmon', 'palegreen', 'darkolivegreen', 'darkgray', 'darkmagenta', 'darkseagreen', 'palegoldenrod', 'sienna', 'darksalmon', 'hotpink', 'lightsteelblue', 'darkturquoise', 'orchid', 'slategray', 'darkslategray', 'lightskyblue', 'mediumorchid', 'lightcoral', 'palevioletred', 'lightgreen', 'tan', 'thistle', 'mistyrose', 'cornsilk']
 
    for i in range(n):
        a = random.randint(5, 10)
        turtle.color(random.choice(colors))
        turtle.pensize(3)
        turtle.penup()
        turtle.goto(random.randint(-280, 280), random.randint(-280, 0))
        turtle.pendown()
        turtle.begin_fill()
        turtle.left(random.randint(0, 180))
        turtle.circle(a, 180)
        turtle.left(45)
        turtle.forward(2 * (math.sqrt((a**2) + (a**2))))
        turtle.right(135)
        turtle.forward(2 * a)
        turtle.right(135)
        turtle.forward(2 * (math.sqrt((a**2) + (a**2))))
        turtle.end_fill()

def draw_bird (n):#doing birds, that have diffrent sizes and positions
    
    for i in range(n): 
        a = random.randint(5, 20)
        turtle.color('black')
        turtle.pensize(5)
        turtle.penup()
        turtle.goto(random.randint(-280, 280), random.randint(0, 280))
        turtle.setheading(random.randint(125, 145) or 135)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(a//2, 45)
        turtle.circle(a, 90)
        turtle.circle(a//2, 45)
        turtle.left(90)
        turtle.circle(a//2, 45)
        turtle.circle(a, 90)
        turtle.circle(a//2, 45)


def draw_big_fish(x, y): #doing the big fish  
    turtle.color('grey')
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.left(45)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(130)
    turtle.right(130)
    turtle.forward(90)
    turtle.left(90)
    turtle.right(90)
    turtle.circle(200,90)
    turtle.left(90)
    turtle.circle(200,90)
    turtle.end_fill()
    turtle.penup()
    turtle.left(130)
    turtle.forward(200)
    turtle.pendown()
    turtle.color('black')
    turtle.begin_fill()
    turtle.circle(10,360)
    turtle.right(270)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()
    turtle.color('black')
    turtle.left(90)
    turtle.circle(100,45)
    turtle.penup()
    turtle.forward(300)
    turtle.left(135)
    turtle.pendown()
    turtle.right(180)


def draw_picture():#code to draw the picture
    draw_background(COL, TAR, WID, HEIG)
    draw_sun(WID)
    draw_waves()
    draw_fish(15)
    draw_bird(15)
    draw_big_fish(0, -100)
    turtle.penup()


draw_picture()
screen.exitonclick()