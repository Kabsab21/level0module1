from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    name = simpledialog.askstring(title='Remarkable', prompt="what is your name?")

    if name == "person1":
        simpledialog.askstring(title='Remarkable', prompt="remarkable thing about person one")

    if name == "person2":
        simpledialog.askstring(title='Remarkable', prompt="remarkable thing about person two")

    if name == "person3":
        simpledialog.askstring(title='Remarkable', prompt="remarkable thing about person three")

