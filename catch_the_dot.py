import turtle
import random

# Pre-generate positions
positions = [(random.randint(-200, 200), random.randint(-200, 200)) for _ in range(1000)]
pos_index = 0
score = 0

# Screen setup
screen = turtle.Screen()
screen.title("Catch the Dot")
screen.bgcolor("white")
screen.tracer(0)

# Dot setup
dot = turtle.Turtle()
dot.shape("circle")
dot.color("red")
dot.penup()
dot.speed(0)

# Score display setup
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 200)
score_display.write("Score: 0", align="center", font=("Arial", 16, "bold"))

def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))

def move_dot(x, y):
    global score, pos_index
    score += 1
    update_score()
    pos_index = (pos_index + 1) % len(positions)
    dot.goto(positions[pos_index])
    screen.update()

# Start game
dot.onclick(move_dot)
dot.goto(positions[0])
update_score()
screen.update()

screen.mainloop()
