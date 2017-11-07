import turtle as t
import random as r

color=[]

def LerpColor(c1,c2,t):
    return (int(c1[0]+(c2[0]-c1[0])*t),int(c1[1]+(c2[1]-c1[1])*t),int(c1[2]+(c2[2]-c1[2])*t))
#color generator입니다.


def genTree(length,level):
    
    if level != 0:
        
     
        t.pensize(level) #level 값에 따라 Pensize가 바뀝니다.

        t.pencolor(color[level])
     
        t.forward(length)

        curPosition = t.position() # 현재 turtle의 위치를 저장
        curHead=t.heading()        # 현재 turtle의 head 방향을 저장

        degree=r.randint(90,180)%90
        t.left(degree/2)           # 왼쪽으로 가지치는 recursion
        """
        여기서 degree값을 상위 레벨 함수에서 받아오지 않고
        
        degree=randint(90, n )%90으로 생성하면 됩니다.
        %90을 하는 이유는 90도를 넘어가게 되면 가지가 너무 꺾여 보기 안좋습니다.
        """
        genTree(length * (r.randint(60,90)/100),level-1)

        """
        여기서 length * 0.7를 하지 않고 length * (randint(60,90)/100)을 해주면
        적당한 범위 내에서 길이를 알아서 줄여줍니다.
        """

        t.penup()                  # turtle의 위치를 원래대로
        t.setposition(curPosition)
        t.setheading(curHead)
        t.pendown()


        degree=r.randint(100,180)%90
        t.right(degree/2)          # 오른쪽으로 가지치는 recursion
        """
        여기서도 degree값을 상위 레벨 함수에서 받아오지 않고
        degree=randint(90, n )%90으로 생성하면 됩니다.
        """
        genTree(length * (r.randint(60,90)/100),level-1)

        """
        여기서도 length * 0.7를 하지 않고 length * (randint(60,90)/100)을 해주면
        적당한 범위 내에서 길이를 알아서 줄여줍니다.
        """

        t.penup()                  # turtle의 위치를 원래대로
        t.setposition(curPosition)
        t.setheading(curHead)
        t.pendown()
        

def main():
    t.hideturtle()
    t.setup(width=.75,height=1.0,startx=0,starty=0)
    
    t.title("Tree Generator using Fractal Copyright 2016. TGISaturday All rights reserved.")
    t.penup()
    t.left(90)
    t.backward(int(t.window_height()/2))      # tree가 시작되는 위치를 설정할 수 있다.
    t.pendown()
    t.clear()
    t.tracer(0.0)       #update가 나오기 전까진 tree를 그리지 않는다.
    
    flag=int(input("Option: 1.Generate random Tree 2.Customize Your Tree:"))
    if flag==1:
        length=r.randint(120,500)
    else:
        length=int(input("Enter the starting length of the branch:"))
        
    level=int(input("Enter the level of branch:"))
    
    maxlen=(0.2*t.window_height())/(1-0.8**(level-1))

    
    if length > maxlen:
        length=maxlen
    t.screensize(int(20*length*(1-0.9**level)),int(length*(1-0.8**(level))))
    
    list_of_colors=[]
    if flag==1:
        for i in range(3):
            list_of_colors.append((r.randint(0,255),r.randint(0,255),r.randint(0,255)))#randint를 활용하여 색의 RGB 값을 자동으로 생성한다.

    else:
        list_of_colors.append(tuple(map(int,input("Enter the RGB value of color 1:").split(','))))
        list_of_colors.append(tuple(map(int,input("Enter the RGB value of color 2:").split(','))))
        list_of_colors.append(tuple(map(int,input("Enter the RGB value of Background color:").split(','))))
    no_steps = level


    for i in range(2):
        for j in range(no_steps):
            color.append(LerpColor(list_of_colors[i],list_of_colors[i+1],j/no_steps))
    t.colormode(255)
    t.bgcolor(list_of_colors[2])
    genTree(length,level)
    t.update()          #tracer와 update를 지우면 tree가 그려지는 과정을 볼 수 있다.
    t.done()
main()
