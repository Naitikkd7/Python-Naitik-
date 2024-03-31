import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Turtle Game")
wn.bgcolor("white")
wn.setup(width=600, height=600)

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.speed(0)
player.goto(0, -250)
player.setheading(90)

# Create obstacles
obstacles = []
for _ in range(5):
    obstacle = turtle.Turtle()
    obstacle.shape("square")
    obstacle.color("red")
    obstacle.penup()
    obstacle.speed(0)
    x = random.randint(-250, 250)
    y = random.randint(100, 250)
    obstacle.goto(x, y)
    obstacles.append(obstacle)

# Set the player's movement speed
player_speed = 15

# Function to move the player left
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)

# Function to move the player right
def move_right():
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)

# Keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

# Main game loop
while True:
    for obstacle in obstacles:
        y = obstacle.ycor()
        y -= 10
        obstacle.sety(y)

        # Check for collision with player
        if player.distance(obstacle) < 20:
            player.hideturtle()
            obstacle.hideturtle()
            print("Game Over")
            wn.bye()

        # Respawn the obstacle if it goes out of the screen
        if y < -300:
            x = random.randint(-250, 250)
            y = random.randint(100, 250)
            obstacle.goto(x, y)

wn.mainloop()
