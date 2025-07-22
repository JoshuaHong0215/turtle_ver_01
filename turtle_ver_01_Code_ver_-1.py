import turtle

# 스크린 생성
s = turtle.getscreen()

# 거북이 변수 지정
t = turtle.Turtle()

# turtle shape style 
t.shape("turtle")
t.shapesize(1.5,1.5,1.5)

# turtle line style 
t.pencolor("purple")
t.pensize(4)

t.goto(0,0)

# 거북이 이동경로 지정
t.penup()
t.goto(-350,-300)
t.pendown()
t.goto(350,300)