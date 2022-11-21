import turtle # 터틀모듈
import random # 랜덤모듈

t = turtle.Turtle()
s = turtle.Screen()
t.speed(0)
def draw_shape(t, c, length, sides, x, y): #함수정의
    t.up()
    t.goto(x, y)  # 좌표이동
    t.down()
    t.fillcolor(c) # 색선정
    angle = 360.0 / sides
    t.begin_fill()
    for dist in range(sides):
        t.forward(length)
        t.left(angle)
    t.end_fill()

for i in range(10):    #도형그리기
    color = random.choice([ 'white', 'yellow', 'blue', 'skyblue', 'orange', 'green' ]) #색 리스트
    side_length = random.randint(10, 100)
    sides = random.randint(3, 10)
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    draw_shape(t, color, side_length, sides, x, y)
