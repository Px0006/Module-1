#drop down menu with a toolbar and status bar
from tkinter import*


def doNothing():
    print("ok ok I won't...")

#######################################################################################
M =                                  'DROPDOWN MENU'
#######################################################################################
    
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

#######################################################################################
T =                                     'TOOLBAR'
#######################################################################################

toolbar = Frame(root, bg='blue')

moistErection = Button(toolbar, text='Insert', command=doNothing)
moistErection.pack(side=LEFT, padx=2, pady=2)
moistErectPack = Button(toolbar, text='Put it in', command=doNothing)
moistErectPack.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X) #display toolbar

#######################################################################################
S =                                     'STATUS BAR'
#######################################################################################

status = Label(root, text="Preparing to do something", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
