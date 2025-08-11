import turtle, random

# Screen setup
screen = turtle.Screen()
screen.title("Catch the Dot")
screen.bgcolor("white")

# Create the dot
dot = turtle.Turtle()
dot.shape("circle")
dot.color("red")
dot.penup()
dot.speed(0)

# Score
score = 0

def move_dot(x, y):
    global score
    score += 1
    print("Score:", score)
    dot.goto(random.randint(-200, 200), random.randint(-200, 200))

# On click
dot.onclick(move_dot)

# Start position
move_dot(0, 0)

screen.mainloop()
