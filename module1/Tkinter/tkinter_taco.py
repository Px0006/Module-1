#message box with a yes or no question with a window
from tkinter import*
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Taco', 'A taco has beef, lettuce, and cheddar cheese')

answer = tkinter.messagebox.askquestion("Question 1", "Do you know what is in a taco?")

in1 = input(' enter here: ')

if answer == "yes":
    print("Excelent: ", in1)
if answer == "no":
    print('A taco has beef, lettuce, and cheddar cheese')

root.mainloop()
