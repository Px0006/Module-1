#images and icons
from tkinter import*

root = Tk()

photo = PhotoImage(file="myface.png")
label = Label(root, image=photo,)
label.pack()

root.mainloop()


