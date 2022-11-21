import turtle # 터틀모듈
import random # 랜덤모듈
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
def draw_star(aturtle, colour, side_length, x, y): # 함수정의
    aturtle.color(colour)
    aturtle.begin_fill()
    aturtle.penup()
    aturtle.goto(x, y) # 좌표이동
    aturtle.pendown()
    for i in range(5):   # 도형그리기
        aturtle.forward(side_length)
        aturtle.right(144)
        aturtle.forward(side_length)
    aturtle.end_fill()

for i in range(20):  # 별20개 그리기
    color = random.choice([ 'white', 'yellow', 'blue', 'skyblue', 'orange', 'green' ]) # 색 리스트
    side_length = random.randint(10, 100)   # 랜던 좌표및 길이 랜덤으로 지정
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    draw_star(t, color, side_length, x, y)  # star함수 실행
