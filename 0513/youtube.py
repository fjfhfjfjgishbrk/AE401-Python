import pytube
import tkinter as tk
import tkinter.ttk


window = tk.Tk()
window.title("wjwkefnjkdjejod")
window.geometry('1000x700')


def showProgress(stream, chunk, bytes_remaining):
    size = yt.streams[0].filesize
    p = 100 - (bytes_remaining / size) * 100
    progressBar['value'] = p
    window.update_idletasks()
    label.config(text="Progress: {}%".format(round(p, 5)))


entry = tk.Entry(window, width=80)
entry.pack()

progressBar = tkinter.ttk.Progressbar(window, orient="horizontal", length=400, mode='determinate')
progressBar.pack()

label = tk.Label(window, text="Progress: ")
label.pack()
choose = False
chooseVar = tk.IntVar()
a = 0
radioButtons = []


def select():
    a = chooseVar.get()


def push():
    global yt
    global choose
    if not choose:
        yt = pytube.YouTube(entry.get(), on_progress_callback=showProgress)
        c = 0
        for i in yt.streams:
            radio = tk.Radiobutton(window, text=i, variable=chooseVar, value=c, command=select)
            radio.pack()
            radioButtons.append(radio)
            c += 1
        chooseVar.set(0)
        choose = True
    else:
        yt.streams[a].download()
        for i in radioButtons:
            i.destroy()
        choose = False


button = tk.Button(text="download", command=push)
button.pack()

window.mainloop()