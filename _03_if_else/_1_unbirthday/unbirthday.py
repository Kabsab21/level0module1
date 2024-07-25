from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    birth = simpledialog.askstring(title='Birth', prompt="what is your birthday? ( mm/dd ex: 03/14 )")

    if birth == "07/25":
        simpledialog.askstring(title='Birth', prompt="happy birthday")

    else:
        simpledialog.askstring(title='Birth', prompt="happy UNbirthday")
