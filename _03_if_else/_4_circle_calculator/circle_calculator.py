# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr

import turtle
from tkinter import messagebox, simpledialog, Tk
import math

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    radius = simpledialog.askinteger(title='circle', prompt="what is the radius in pixels?")

    calcu = simpledialog.askstring(title='circle', prompt="Do you want to calculate the area or the circumference( answer area or circ )?")

    turtle1 = turtle.Turtle()

    turtle1.circle(radius,  1000)

    turtle1.penup()

    turtle1.goto( 100, 100)

    area = (radius * radius) * math.pi
    circ = 2 * math.pi * radius

    if calcu == "circ":
        turtle1.write(arg="circumference = " + str(circ), move=True, align='left', font=('Arial', 18, 'normal'))
    if calcu == "area":
         turtle1.write(arg="area = " + str(area), move=True, align='left', font=('Arial', 18, 'normal'))


    turtle1.hideturtle()

    turtle.done()
