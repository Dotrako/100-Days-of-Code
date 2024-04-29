from turtle import Turtle, Screen

tim = Turtle()









screen = Screen()

def move_forwrad():
    tim.forward(10)

def backwards():
    tim.backward(10)

def counter_clockwise():
    tim.left(10)
    




screen.listen()
screen.onkey(key = "space", fun = move_forwrad)
screen.onkey(key = "s", fun=backwards)
screen.onkey(key = "a", fun = counter_clockwise)

screen.exitonclick()