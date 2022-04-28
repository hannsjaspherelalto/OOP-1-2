from tkinter import *

tab = Tk()

tab.title("Special Midterm Exam in OOP")
tab.geometry("700x500+20+10")


def magic():
    btn.configure(bg="yellow")


btn = Button(tab, text="Click to Change Color", command=magic)

btn.place(x=350, y=250, anchor="center")


tab.mainloop()