import turtle

# Setting up window
window = turtle.Screen()
window.title('Pong')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0)

# Player 1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape('square')
player1.color('white')
player1.shapesize(stretch_wid=5, stretch_len=1)
player1.penup()
player1.goto(-350, 0)
player1.dy = 0

# Player 2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape('square')
player2.color('white')
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.penup()
player2.goto(350, 0)
player2.dy = 0

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)

ball.dx = 0.3
ball.dy = 0.3

# Functions
def updatePlayers():
    player1Y = player1.ycor()
    player1Y += player1.dy
    player1.sety(player1Y)

    player2Y = player2.ycor()
    player2Y += player2.dy
    player2.sety(player2Y)

def player1Up():
    #y = player1.ycor()
    #y += 20
    #player1.sety(y)
    player1.dy = 1

def player1Down():
    #y = player1.ycor()
    #y -= 20
    #player1.sety(y)
    player1.dy = -1

def stopPlayer1():
    player1.dy = 0

def player2Up():
    #y = player2.ycor()
    #y += 20
    #player2.sety(y)
    player2.dy = 1

def player2Down():
    #y = player2.ycor()
    #y -= 20
    #player2.sety(y)
    player2.dy = -1

def stopPlayer2():
    player2.dy = 0


def moveBall():
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

def checkBallCollision():
    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.dx *= -1
        ball.goto(0, 0)

    if ball.xcor() < -390:
        ball.dx *= -1
        ball.goto(0, 0)

    if (ball.xcor() >= 340 and ball.xcor() <= 360) and (ball.ycor() - 10 <= player2.ycor() + 50 and ball.ycor() + 10 >= player2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() <= -340 and ball.xcor() >= -360) and (ball.ycor() - 10 <= player1.ycor() + 50 and ball.ycor() + 10 >= player1.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1

# Events
window.listen()
window.onkeypress(player1Up, 'w')
window.onkeypress(player1Down, 's')
window.onkeypress(player2Up, 'Up')
window.onkeypress(player2Down, 'Down')

window.onkeyrelease(stopPlayer1, 'w')
window.onkeyrelease(stopPlayer1, 's')
window.onkeyrelease(stopPlayer2, 'Up')
window.onkeyrelease(stopPlayer2, 'Down')

# Main loop
while True:
    window.update()
    updatePlayers()
    checkBallCollision()
    moveBall()