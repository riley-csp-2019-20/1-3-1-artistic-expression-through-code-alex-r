import turtle as trtl
import random as ra
wn = trtl.Screen()

shape = "arrow"
arrow = trtl.Turtle(shape = shape) 
#Variables
count = 1
turtlespeed = 10

print("Welcome to my game. Press the arrow key that corresponds to the arrow. This game is endless, have fun :)") #Intro message

def turtle_up():        #These are the movement functions for the turtle
    arrow.setheading(90)
    arrow.forward(100)
def turtle_down():
    arrow.setheading(270)
    arrow.forward(100)
def turtle_right():
    arrow.setheading(0)
    arrow.forward(100)
def turtle_left():
    arrow.setheading(180)
    arrow.forward(100)

arrow_list = [] # This list stores the number that corresponds to a direction. The check functions use this list

def c_turtle_up():   #These check the list to see if the key pressed is correct (This is like the Apple Avalanche code)
    if(1 in arrow_list):
        arrow_list.clear()
        # print("up")
        starting_gate()

def c_turtle_down():
    if(2 in arrow_list):
        arrow_list.clear()
        # print("down")
        starting_gate()

def c_turtle_right():
    if(3 in arrow_list):
        arrow_list.clear()
        # print("left")
        starting_gate()
def c_turtle_left():
    if(4 in arrow_list):
        arrow_list.clear()
        # print("right")
        starting_gate()

def starting_gate():  # This function is where the magic happens. It adds a random number from 1-4 to a list and makes the turtle go in the corresponding direction.
    arrow.speed(0)
    arrow.goto(0,0)
    arrow.speed(turtlespeed)    
    r_number = ra.randint(1,4)
    if r_number == 1:
        turtle_up()
        arrow_list.append(1)
    elif r_number == 2:
        turtle_down()
        arrow_list.append(2)
    elif r_number == 3:
        turtle_right()
        arrow_list.append(3)
    elif r_number == 4:
        turtle_left()
        arrow_list.append(4)
    # print(arrow_list)

one_tap = 0   # This bit of code starts the loop. It only needs to call the function once because the checker starts the code over and over
if one_tap < 1:
    starting_gate()
    one_tap + 1

wn.onkeypress(c_turtle_up, "Up")   # In order to reset the turtle, you need to click the corresponding arrow key.
wn.onkeypress(c_turtle_down, "Down")
wn.onkeypress(c_turtle_right, "Right")
wn.onkeypress(c_turtle_left, "Left")

wn.onkeypress(c_turtle_up, "w")   # You can also use wasd 
wn.onkeypress(c_turtle_down, "s")
wn.onkeypress(c_turtle_right, "d")
wn.onkeypress(c_turtle_left, "a")

wn.listen()
wn.mainloop()  