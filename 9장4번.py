import turtle
import random
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

def draw_square(x, y, c):    # 사각형을 그리는 함수
    t.up()               
    t.goto(x, y)             # (x,y) 좌표이동
    t.down()
    t.color("black",c)
    t.begin_fill()          # 색을 채우기 시작함
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.end_fill()
for c in ["yellow", "red", "purple", "blue"]:  #리스트에 저장된 색이 순서대로 표현
    x = random.randint(-100, 100)  # x의 좌표 값
    y = random.randint(-100, 100)  # y의 좌표 값
    draw_square(x, y, c)
