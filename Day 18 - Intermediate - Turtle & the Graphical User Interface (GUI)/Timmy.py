# from turtle import Turtle, Screen

# timmy_the_turtle = Turtle()

# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red", "green")
# timmy_the_turtle.forward(90)
# timmy_the_turtle.right(90)
# timmy_the_turtle.back(90)
# timmy_the_turtle.left(90)
# timmy_the_turtle.back(90)
# timmy_the_turtle.left(90)
# timmy_the_turtle.back(90)

# # or with a loop

# for i in range(4):
#     timmy_the_turtle.forward(90)
#     timmy_the_turtle.left(90)

# screen_object = Screen()
# screen_object.exitonclick()


# import heroes
# print(heroes.gen())

# from heroes import *

# from heroes import gen


# Drawing a Dashed Line Challenge
# importing necessary libraries

# from turtle import Turtle as T
# from turtle import Screen as S

# tim = T()
# tim.shape("Turtle")
# tim.color("red", "green")


# screen = S()
# screen.exitonclick()


# from turtle import Turtle , Screen


# my_pet = Turtle()
# my_pet.shape("turtle")
# my_pet.color("Red","Green")


# for i in range(4):
#     my_pet.forward(100)
#     my_pet.left(90)


# display = Screen()
# display.exitonclick()



# we want to write a script for  a turtle that will right one _ and then jump to do a shape like this: _ _ _ _ _ _ _ _

from turtle import Turtle, Screen

# Creating the turtle using the Turtle library method

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")

for i in range(5):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()



display = Screen()
display.exitonclick()

