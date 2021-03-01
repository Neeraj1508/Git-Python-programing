from vpython import *
canvas(background = color.magenta)
donut = ring(radius = 0.6, thickness = 0.26, color = vector(400, 100, 1))
choclate = ring(radius = 0.7, thickness = 0.26, color = vector(0.4, 0.2, 0))
rad = 0
while True:
    rate(10)
    # donut.rotate(angle = rad, axis = vector(0.5, 1, -0.5))
    # choclate.rotate(angle = rad, axis = vector(0.5, 1, -0.5))
    donut.pos = vector(3*cos(rad), sin(rad), 0)
    choclate.pos = vector(3*cos(rad), sin(rad), 0)
    rad = rad + 0.03