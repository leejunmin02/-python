import turtle
import random

def screenLeftClick(x,y):
     tSize = random.randrange(2,10) //변수 tSize는 2~10의 랜덤한 수를 가진다.
     turtle.shapesize(tSize)  // 거북이모양의 크기를 tSize만큼 설정한다
     r = random.random() // 변수 r는 랜덤한 수를 가진다.
     g = random.random()//변수 g는 랜덤한 수를 가진다.
     b = random.random()//변수 b는 랜덤한 수를 가진다.
     turtle.color((r, g, b)) //거북이의 색을 r,g,b로설정한다.
     tAngle = random.randrange(0, 360) 0~360의 범위에서 랜덤한 수를 반환한다.

     turtle.penup() //펜을 올린다.
     turtle.goto(x,y) //펜을 x,y로 이동한다
     turtle.left(tAngle) //거북이를 왼쪽으로 tAngle만큼 회전한다
     turtle.stamp() //도장을 찍는다.


tultle.shape('turtle') //거북이 모양으로 설정한다
turtle.pensize(10) //펜크기를 10으로 설정한다
turtle.screemLeftCilck(screenLeftclick,1) //클릭 시 screenLeftClick을 왼쪽클릭을 할 때 실행한다. 

turtle.done()