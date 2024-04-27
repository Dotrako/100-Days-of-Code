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
import random

# Creating the turtle using the Turtle library method

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("green")

# for i in range(5):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()



# display = Screen()
# display.exitonclick()


# Creating a shaped hexagon

# timmy = Turtle()
# timmy.shape("turtle")

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SlateGray", "SeaGreen"]



# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
    

# for shape_side_n in range(3,11):
#     timmy.color(random.choice(colours))
#     draw_shape(shape_side_n)

# display = Screen()
# display.exitonclick()

# import turtle as t
# import random

# tim = t.Turtle()
# tim.shape("circle")
# t.colormode(255)

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r, g, b)
#     return random_color


# directions = [0, 90 , 180, 270]
# tim.pensize(15)
# tim.speed("fastest")

# for i in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


# display = t.Screen()
# display.exitonclick()

# import turtle as t
# import random

# tim = t.Turtle()
# tim.shape("turtle")
# t.colormode(255)

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     color = (r, g, b)
#     return color


# tim.circle(100)
# tim.right(75)
# tim.back(100)
# tim.speed("fastest")




# display = t.Screen()
# display.exitonclick()

import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color


tim.speed("fastest")

for _ in range(100):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + 10)



display = t.Screen()
display.exitonclick()
