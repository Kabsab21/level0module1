import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    radius = simpledialog.askinteger(title='circle', prompt="what is the radius in pixels?")
    
    # Make a new turtle
    turtle1 = turtle.Turtle()
    # Have your turtle draw a circle with the correct radius
    turtle1.circle(radius,  1000)

    # Call the turtle .penup() method
    turtle1.penup()
    # Move your turtle to a new x,y position using .goto()
    turtle1.goto( 100, 100)
    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    area = (radius * radius) * math.pi
    # Write the area of your circle using the turtle .write() method
    turtle1.write(arg="area = " + str(area), move=True, align='left', font=('Arial', 18, 'normal'))

    # Hide your turtle
    turtle1.hideturtle()
    # Call turtle.done()
    turtle.done()
