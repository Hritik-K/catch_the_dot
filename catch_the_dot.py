import turtle
import random

# Pre-generate random positions for faster movement
positions = [(random.randint(-200, 200), random.randint(-200, 200)) for _ in range(1000)]
pos_index = 0
score = 0

# Screen setup
screen = turtle.Screen()
screen.title("Catch the Dot")
screen.bgcolor("white")
screen.tracer(0)  # Turn off auto updates for speed

# Dot setup
dot = turtle.Turtle()
dot.shape("circle")
dot.color("red")
dot.penup()
dot.speed(0)

def move_dot(x, y):
    global score, pos_index
    score += 1
    pos_index = (pos_index + 1) % len(positions)
    dot.goto(positions[pos_index])
    screen.update()  # Manual update for instant refresh

dot.onclick(move_dot)

# Start position
dot.goto(positions[0])
screen.update()

screen.mainloop()
