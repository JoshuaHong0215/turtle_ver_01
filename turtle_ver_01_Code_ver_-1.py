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

# 장애물 회피 기동_ver_01
# t.forward(100)
# t.setheading(45)
# t.forward(500)
# t.setheading(-45)
# t.forward(150)
# t.setheading(45)
# t.forward(150)

# 장애물 회피 기동_ver_03
# t.forward(300)
# t.setheading(135)
# t.forward(150)
# t.setheading(45)
# t.forward(350)
# t.setheading(-45)
# t.forward(150)
# t.setheading(45)
# t.forward(200)

# 함수 지정
distance_list = []

def custom_forward(turtle_obj, dist):
    turtle_obj.forward(dist)
    distance_list.append(dist)
# -------------------------------------------

# 장애물 회피 기동_ver_02
custom_forward(t, 300)
t.setheading(135)
custom_forward(t, 150)
t.setheading(45)
custom_forward(t, 350)
t.setheading(-45)
custom_forward(t, 150)
t.setheading(45)
custom_forward(t, 200)

# 이동 거리 출력
total_distance = sum(distance_list)
print(f"총 이동 거리: {total_distance} 픽셀")