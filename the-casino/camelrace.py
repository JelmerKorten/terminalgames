# using turtle to create a camel race that can be bet on.
# no controls to "help" the camel yet.

import turtle as t
import time

WIDTH, HEIGHT = 600, 600

t.screensize(WIDTH,HEIGHT)
arr1 = t.Turtle()
arr2 = t.Turtle()

for _ in range(4):
    arr1.forward(50)
    arr1.left(90)
    arr1.forward(50)
    arr1.left(90)
    arr2.forward(50)
    arr2.left(90)

time.sleep(5)
