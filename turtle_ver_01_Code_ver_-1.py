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

# 거북이 이동경로 지정
t.penup()
t.goto(-350,-300)
# t.pendown()
# t.goto(350,300)