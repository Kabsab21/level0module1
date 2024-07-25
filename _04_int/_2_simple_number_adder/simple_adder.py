"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""

from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    num1 = simpledialog.askstring(title='CALCULATOR', prompt="give number")
    num2 = simpledialog.askstring(title='CALCULATOR', prompt="give number again ")
    ans = int(num1) + int(num2)
    simpledialog.askstring(title='CALCULATOR', prompt=" sum is "+str(ans)+".")
