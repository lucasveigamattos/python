import turtle

# Setting up window
window = turtle.Screen()
window.title('Mario')
window.setup(width=800, height=400)
window.tracer(0)

# Player
player = turtle.Turtle()
player.shape('square')
player.color('black')
player.penup()
player.goto(0, 0)

player.dx = 0
player.dy = 0

# Functions
def updatePlayer(gravity):
    player.setx(player.xcor() + player.dx)
    player.sety(player.ycor() + player.dy)

    if player.ycor() - 10 + player.dy <= -(window.window_height() / 2 - 10):
        player.dy = 0
    else:
        player.dy += gravity

def moveToRight():
    player.dx = 0.2

def moveToLeft():
    player.dx = -0.2

def jump():
    if player.dy == 0:
        player.dy = 0.5

def stopPlayer():
    player.dx = 0

# Events
window.listen()
window.onkeypress(moveToRight, 'Right')
window.onkeypress(moveToLeft, 'Left')
window.onkeypress(jump, 'Up')
window.onkeyrelease(stopPlayer, 'Right')
window.onkeyrelease(stopPlayer, 'Left')

# Main loop
while True:
    window.update()
    updatePlayer(-0.001)