"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""

from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    num1 = simpledialog.askstring(title='CALCULATOR', prompt="give number")
    type = simpledialog.askstring(title='CALCULATOR', prompt="add sub mult or div?")
    num2 = simpledialog.askstring(title='CALCULATOR', prompt="give number again ")

    if type == "add":
         ans = int(num1) + int(num2)
         simpledialog.askstring(title='CALCULATOR', prompt=" sum is "+str(ans)+".")
    elif type == "sub":
         ans = int(num1) - int(num2)
         simpledialog.askstring(title='CALCULATOR', prompt=" answer is "+str(ans)+".")
    elif type == "mult":
         ans = int(num1) * int(num2)
         simpledialog.askstring(title='CALCULATOR', prompt=" product is "+str(ans)+".")
    elif type == "div":
         ans = int(num1) / int(num2)
         simpledialog.askstring(title='CALCULATOR', prompt=" answer is "+str(ans)+".")

