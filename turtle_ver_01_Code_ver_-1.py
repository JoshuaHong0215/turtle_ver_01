import turtle
import random

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


# 이동거리 함수 지정
distance_list = []

def custom_forward(turtle_obj, dist):
    turtle_obj.forward(dist)
    distance_list.append(dist)

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
#----------------------------------------------------------
# 장애물 회피 함수
def avoid_obstacle():
    """장애물을 회피하는 행동을 수행합니다."""
    print("🚨 장애물 감지! 회피 행동 시작!")

    # 1단계: 랜덤한 회전 각도 생성 (30~150도)
    turn_angle = random.randint(30, 150)
    print(f"회전 각도: {turn_angle}도")

    # 2단계: 좌회전 또는 우회전 랜덤 선택
    direction = random.choice([1, -1])  # 1=좌회전, -1=우회전
    if direction == 1:
        t.left(turn_angle)
        print(f"좌회전 {turn_angle}도")
    else:
        t.right(turn_angle)
        print(f"우회전 {turn_angle}도")

    # 3단계: 회전 후 안전 거리만큼 이동
    move_distance = random.randint(20, 50)
    t.forward(move_distance)
    print(f"{move_distance}픽셀 이동 완료")
    distance_list.append(move_distance)
#-------------------------------------------
    # 랜덤 워크 + 충돌 회피 + 도착 판단
goal_x = 250
goal_y = 300

step_size = 20
max_steps = 1000

for step in range(max_steps):
    if reached_destination(t, goal_x, goal_y):
        print("🎯 도착 지점에 도달했습니다.")
        break

    # 랜덤한 방향으로 움직이기
    angle_to_goal = t.towards(goal_x, goal_y)
    random_offset = random.randint(-30, 30)  # ±30도 정도 오차
    t.setheading(angle_to_goal + random_offset)

    # 이동
    t.forward(step_size)
    distance_list.append(step_size)

    # 충돌 감지 → 회피
    if check_collision(t):
        print("❌ 충돌 감지! 되돌아갑니다.")
        t.backward(step_size)
        avoid_obstacle()
#------------------------------------------------------------------------------

# 이동 거리 출력
total_distance = sum(distance_list)
print(f"총 이동 거리: {total_distance} 픽셀")



# 사용


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

