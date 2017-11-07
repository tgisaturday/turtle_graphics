def koch(order,size):
    """
    make turtle t draw a Koch fractal of 'order' and 'size'.
    Leave the turtle facing the same direction.
    """
    if order ==0:   #the base case is just a straight line
        forward(size)
    else:
        koch(order-1,size/3) #Go 1/3 of the way
        left(60)
        koch(order-1,size/3)
        right(120)
        koch(order-1,size/3)
        left(60)
        koch(order-1,size/3)

from turtle import *
level=int(input("Insert level of the Koch curve:"))
length=int(input("Insert total length of the Koch curve:"))
my_start=(-length/2,length/4)
penup()
setx(my_start[0])
sety(my_start[1])
pendown()
tracer(0,0)
koch(level,length)
right(120)
koch(level,length)
right(120)
koch(level,length)
update()
done()

