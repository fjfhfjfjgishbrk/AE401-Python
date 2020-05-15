import tkinter as tk
import tkinter.messagebox
import random

colorArray = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
window = tk.Tk()


def randomColor():
    a = ["#"]
    for i in range(6):
        a.append(colorArray[random.randrange(len(colorArray))])
    return "".join(a)


labelColor = randomColor()
windowColor = randomColor()
pushChange = False


def push():
    global pushChange
    pushChange = False if pushChange else True
    if pushChange:
        label.config(bg=windowColor)
    else:
        label.config(bg=labelColor)


def changeColor():
    global windowColor
    windowColor = randomColor()
    window.configure(bg=windowColor)
    window.title(windowColor)
    tkinter.messagebox.showinfo(title="wjefnk", message="Color changed to {}".format(windowColor))


window.title(windowColor)
window.geometry('400x400')
window.configure(bg=windowColor)

label = tk.Label(window, text="sjdnkwef", bg=labelColor)
label.pack()

entry = tk.Entry(window, width=39)
entry.pack()

button = tk.Button(text="button", command=push)
button.pack()

string = tk.StringVar()


def select():
    label.config(text=string.get())


radio1 = tk.Radiobutton(window, text='X', variable=string, value="ajksdnw", command=select)
radio2 = tk.Radiobutton(window, text='Y', variable=string, value="frefjks", command=select)
radio1.pack()
radio2.pack()
string.set("ajksdnw")

menu = tk.Menu(window)
subMenu = tk.Menu(menu, tearoff=False)
subMenu.add_command(label="color", command=changeColor)
subMenu.add_command(label="rfjnksndc")
subMenu.add_separator()
subSubMenu = tk.Menu(subMenu, tearoff=False)
subSubMenu.add_command(label="wjefnbjk")
subMenu.add_cascade(label="sjekfk", menu=subSubMenu)
subMenu.add_command(label="ejdksnc")
menu.add_cascade(label="A", menu=subMenu)

window.config(menu=menu)

window.mainloop()
