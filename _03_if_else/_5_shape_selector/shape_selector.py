import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    turtle1 = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title='Shape selector', prompt="what shape do you want to draw?")
    # Draw the shape requested by the user using if-elif-else statements
    turtle1.pendown
    turtle1.color( "black")
    if shape == "square":
        for i in range(4):
            turtle1.forward(50)
            turtle1.right(90)
    elif shape == "triangle":
            turtle1.forward(50)
            turtle1.right(120)
            turtle1.forward(50)
            turtle1.right(120)
            turtle1.forward(50)

    elif shape == "circle":
        turtle1.circle(50, 1000)
    else:
        simpledialog.askstring(title='Shape selector', prompt="we cannot make a shape such as this, please exit and try again.")
    # Call the turtle .done() method
    turtle.done()
