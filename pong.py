import turtle

# Вікно
window = turtle.Screen()
window.title("My game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Ліва_ракетка
racket_a = turtle.Turtle()
racket_a.speed(0)
racket_a.shape("square")
racket_a.color("red")
racket_a.shapesize(stretch_len=1, stretch_wid=5)
racket_a.penup()
racket_a.goto(-350, 0)

# Права_ракетка
racket_b = turtle.Turtle()
racket_b.speed(0)
racket_b.shape("square")
racket_b.color("yellow")
racket_b.shapesize(stretch_len=1, stretch_wid=5)
racket_b.penup()
racket_b.goto(350, 0)

# м'ячик
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3


# рахунок
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 || Player B: 0", align="center", font=("Verdana", 22, "normal"))

score_a = 0
score_b = 0

# Рух ракетки з права
def racket_a_up():
    y = racket_a.ycor()
    # щоб не виходило за границі
    if y > 240:
        y.set(240)
        y.dy *= -1
    y += 20
    racket_a.sety(y)

def racket_a_down():
    y = racket_a.ycor()
    # щоб не виходило за границі
    if y < -240:
        y.set(-240)
        y.dy *= -1
    y -= 20
    racket_a.sety(y)

# Рух ракетки з ліва
def racket_b_up():
    y = racket_b.ycor()
    # щоб не виходило за границі
    if y > 240:
        y.set(240)
        y.dy *= -1
    y += 20
    racket_b.sety(y)

def racket_b_down():
    y = racket_b.ycor()
    # щоб не виходило за границі
    if y < -240:
        y.set(-240)
        y.dy *= -1
    y -= 20
    racket_b.sety(y)

# клавіатура
window.listen()
window.onkeypress(racket_a_up, "w")
window.onkeypress(racket_a_down, "s")
window.onkeypress(racket_b_up, "Up")
window.onkeypress(racket_b_down, "Down")

# щоб вікно не пропадало
while True:
    window.update()

    # Рух мячика
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # щоб мячик не виходив за верхню частину поля
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # щоб мячик не виходив за нижню частину поля
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # щоб мячик не виходив за праву частину поля і вертався в центр
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} || Player B: {}".format(score_a, score_b), align="center", font=("Verdana", 22, "normal"))

    # щоб мячик не виходив за ліву частину поля і вертався в центр
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} || Player B: {}".format(score_a, score_b), align="center", font=("Verdana", 22, "normal"))

    # щоб мячик бачив ракетки
    if ball.xcor() > 340 and ball.ycor() < racket_b.ycor() + 50 and ball.ycor() > racket_b.ycor() - 50:
        ball.dx *= -1

    if ball.xcor() < -340 and ball.ycor() < racket_a.ycor() + 50 and ball.ycor() > racket_a.ycor() - 50:
        ball.dx *= -1
