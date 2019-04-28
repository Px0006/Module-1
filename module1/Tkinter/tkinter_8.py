#message box with a yes or no question with a window
from tkinter import*
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("window Title", "Python is awesome and you shoud love it")

answer = tkinter.messagebox.askquestion("Question 1", "Do you want an apple?")

if answer == "yes":
    print("<|@^@|>")
if answer == "no":
    print("Boooo!")

root.mainloop()
