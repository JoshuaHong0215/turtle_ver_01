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

# 도착 지점 판별 함수 추가
def reached_destination(turtle_obj, goal_x, goal_y, tolerance=10):
    """
    turtle_obj: 거북이 객체
    goal_x, goal_y: 도착 지점 좌표
    tolerance: 오차 범위 (도착 판정 시 허용)
    """
    x, y = turtle_obj.pos()
    return abs(x - goal_x) <= tolerance and abs(y - goal_y) <= tolerance

# 충돌 감지 함수 추가
def check_collision(turtle_obj, margin=10):
    x, y = turtle_obj.pos()
    # 장애물 좌표 영역: x [-50, 50], y [0, 100]
    if (-50 - margin) <= x <= (50 + margin) and (0 - margin) <= y <= (100 + margin):
        return True
    return False

# 사용
goal_x = 250
goal_y = 300

if reached_destination(t, goal_x, goal_y):
    print("도착 지점에 도달했습니다.")
else:
    print("아직 도착하지 않았습니다.")
    
print("현재 거북이 위치:", t.pos())  # 현재 거북이의 좌표를 출력하는 함수


# 충돌 판정
if check_collision(t):
    print("아아아아아아아아아아아아아아악")
    
else:
    print("나이스")