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

# 장애물 설치
t.penup()
t.goto(-50,100)
t.pendown()
t.setheading(0)
t.fillcolor("red")
t.begin_fill()
for _ in range(2):
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    
t.end_fill()

# 거북이 시작점 및 자세지정 세팅
t.penup()
t.goto(-350,-300)
t.setheading(45)
t.pendown()

# 장애물 회피 기동 
t.goto(-200,-150)
t.setheading(135)
t.forward(150)
t.setheading(45)
t.forward(500)
t.setheading(-45)
t.forward(150)
t.setheading(45)
t.forward(150)