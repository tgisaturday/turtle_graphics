import turtle as t

def genTree(length, level):
    if level !=0:

        t.pensize(level)
        t.forward(length)
        curPosition=t.position()
        curHead=t.heading()

        t.left(30)
        genTree(int(length*0.9),level-1)

        t.penup()
        t.setposition(curPosition)
        t.setheading(curHead)
        t.pendown()

        lev=level-1
        if lev!=0:
            t.pensize(lev)
            t.right(90)
            genTree(int(length*0.5),lev-1)
            t.penup()
            t.setposition(curPosition)
            t.setheading(curHead)
            t.pendown()

def main():
    t.hideturtle()
    t.penup()
    t.left(90)
    t.backward(250)
    t.pendown()
    t.clear()
    t.tracer(0.0)   
    
    length=int(input("Enter the starting length of the branch:"))
    level=int(input("Enter the level of branch:"))
    genTree(length,level)
    t.update()
    t.done()

main()
        
