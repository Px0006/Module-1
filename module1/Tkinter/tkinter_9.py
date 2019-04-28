#shapes and graphics
from tkinter import*

root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

blackLine = canvas.create_line(0, 0, 200, 50)
redLine = canvas.create_line(0, 100, 200, 50, fill="red")

greenBox = canvas.create_rectangle(25, 25, 130, 60, fill="green") #top left of rectangle, go over 25, go down 25 as a starting point. Create a width of 130 and a height of 60 pixels. Fill in the rectangle green

#canvas.delete(redLine)
#canvas.delete(ALL)

root.mainloop()
