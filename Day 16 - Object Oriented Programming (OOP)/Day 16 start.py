# from anothermodule import x
# print(x+1)

# import anothermodule 
# print(anothermodule.x)

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")

# turtle color
timmy.color("red", "green")

# # moving my freind timmy 
# timmy.forward(100) # fd() can also work
# timmy.left(100) 
# timmy.back(200) # bk()
# timmy.right(200)

# Draw a square with Timmy
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()