from turtle import *

HEIGHT, WIDTH = 180, 180
ITERATION = 100
screen = Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)
screen.screensize(WIDTH, HEIGHT)
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)

tu = Turtle()
tu.hideturtle()
tu.speed(100)
tu.penup()

screen.tracer(False)


def mapPoint(n, start1, stop1, start2, stop2):
    return ((n - start1) / (stop1 - start1)) * (stop2 - start2) + start2


for x in range(WIDTH):
    for y in range(HEIGHT):

        realComponent = mapPoint(x, 0, WIDTH, -2, 2)
        imaginaryComponent = mapPoint(y, 0, HEIGHT, -2, 2)
        ca = realComponent
        cb = imaginaryComponent

        n = 0
        z = 0
        while n < ITERATION:
            aa = realComponent * realComponent - imaginaryComponent * imaginaryComponent
            bb = 2 * realComponent * imaginaryComponent

            realComponent = aa + ca
            imaginaryComponent = bb + cb
            n += 1

            if abs(realComponent + imaginaryComponent) > 16:
                break

        bright = 'pink'
        if n == ITERATION:
            bright = 'black'

        tu.goto(x, y)
        tu.pendown()
        tu.dot(4, bright)
        tu.penup()

screen.update()
screen.tracer(True)
done()
