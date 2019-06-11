from turtle import Turtle, Screen
from time import time


def mapPoint(number, start1, stop1, start2, stop2):
    """
    This method maps the number number between start2 and stop2 with the same ratio it had between start1 and start2.
    @:param number: is the mapped number
    @:param start1: is the lowest value of the range in which number is
    @:param stop1: is the highest value of the range in which number is
    @:param start2: is the lowest value of the range in which number is going to be
    @:param stop2: is the highest value of the range in which number is going to be
    @:return the calculated number
    """
    return ((number - start1) / (stop1 - start1)) * (stop2 - start2) + start2


HEIGHT, WIDTH = 350, 360  # Set screen width and height
ITERATION = 100  # Set max iterations

screen = Screen()
screen.setup(WIDTH, HEIGHT)  # Setup the screen
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)  # Set origin of the turtle in the bottom left corner

tu = Turtle()
tu.hideturtle()
tu.speed(0)
tu.penup()

screen.tracer(False)  # Set screen tracer to false to speed up the process to draw the mandelbrot set

startTime = time()  # Get the current time

for x in range(WIDTH):  # Loop through every pixel in the width

    for y in range(HEIGHT):  # Loop through every pixel in the height

        realComponent = mapPoint(x, 0, WIDTH, -2, 2)  # Map the x coordinate between -2 and 2
        imaginaryComponent = mapPoint(y, 0, HEIGHT, -2, 2)  # Map the y coordinate between -2 and 2
        startedRealComponent = realComponent
        startedImaginaryComponent = imaginaryComponent

        iterationsDone = 0
        while iterationsDone < ITERATION:
            complexNumberA = realComponent * realComponent - imaginaryComponent * imaginaryComponent  # A squared real number - a squared imaginary number to get a complex number
            complexNumberB = 2 * realComponent * imaginaryComponent

            realComponent = complexNumberA + startedRealComponent  # Add the start number to the complex number A
            imaginaryComponent = complexNumberB + startedImaginaryComponent  # Add the start number to the complex number B
            iterationsDone += 1

            if abs(
                    realComponent + imaginaryComponent) > 16:  # If realComponent + the imaginaryComponent is bigger than 16 the number is not in the range of the mandelbrot set, so the while loop breaks and a grey pixel is drawn.
                break

        color = 'grey'
        if iterationsDone == ITERATION:  # If the while loop got executed 100 times, the complex number is in the range of the mandelbrot set so a black point is drawn
            color = 'black'

        tu.goto(x, y)  # Move the turtle to x and y cors
        tu.pendown()
        tu.dot(4, color)  # Draw a point with the certain color
        tu.penup()

screen.update()  # Update the screen to add the drawn stuff to the screen
screen.tracer(True)  # Set screen tracer to true to see the result
endTime = time()  # Get current time
print("Draw finish, elapsed time: ", endTime - startTime,
      "sec")  # Calc time elapsed and print a msg that the drawing is finished
screen.exitonclick()
