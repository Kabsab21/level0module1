"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    correct = 0
    ans = simpledialog.askstring(title='RIDDLE', prompt="riddle number 1")
    if ans == "1":
        correct = correct+1
    ans = simpledialog.askstring(title='RIDDLE', prompt="riddle number 2")
    if ans == "2":
        correct = correct+1
    ans = simpledialog.askstring(title='RIDDLE', prompt="riddle number 3")
    if ans == "3":
        correct = correct+1

    simpledialog.askstring(title='RIDDLE', prompt="You answered "+str(correct)+" riddles correctly")
