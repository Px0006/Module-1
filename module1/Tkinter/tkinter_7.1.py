#drop down menu
from tkinter import*


def doNothing():
    print("ok ok I won't...")
    
root =Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu) #sub menu in menu
menu.add_cascade(label="File", menu=subMenu) #create a drop down menu inside submenu
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="Now...", command=doNothing)
subMenu.add_separator() #submenu 
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

root.mainloop()
