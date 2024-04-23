from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red", "green")
timmy_the_turtle.forward(90)
timmy_the_turtle.right(90)
timmy_the_turtle.back(90)
timmy_the_turtle.left(90)
timmy_the_turtle.back(90)
timmy_the_turtle.left(90)
timmy_the_turtle.back(90)

# or with a loop

for i in range(4):
    timmy_the_turtle.forward(90)
    timmy_the_turtle.left(90)

screen_object = Screen()
screen_object.exitonclick()


