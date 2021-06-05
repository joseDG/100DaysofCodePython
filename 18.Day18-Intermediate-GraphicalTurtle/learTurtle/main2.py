import turtle as t
import  random

tim = t.Turtle()

colours = ["cyan", "chartreuse", "brown", "cornflower blue", "dark violet", "sandy brown", "lawn green"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))

