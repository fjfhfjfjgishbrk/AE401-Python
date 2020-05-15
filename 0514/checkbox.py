import pytube
import tkinter as tk
import tkinter.ttk
import threading


window = tk.Tk()
window.title("wjwkefnjkdjejod")
window.geometry('1000x700')


def showProgress(stream, chunk, bytes_remaining):
    for i in range(3):
        size = yt[i].streams[0].filesize
        p = 100 - (bytes_remaining / size) * 100
        progressBarArray[i]['value'] = p
        labelArray[i].config(text="Progress: {}%".format(round(p, 5)))
    window.update_idletasks()


def th():
    threading.Thread(target=push).start()


entryArray = []
checkArray = []
checkVarArray = []
progressBarArray = []
labelArray = []
for i in range(3):
    entry = tk.Entry(window, width=80)
    entry.pack()
    entryArray.append(entry)
    checkVar = tk.IntVar()
    check = tk.Checkbutton(window, text="download", variable=checkVar)
    check.pack()
    checkArray.append(check)
    checkVarArray.append(checkVar)
    progressBar = tkinter.ttk.Progressbar(window, orient="horizontal", length=400, mode='determinate')
    progressBar.pack()
    progressBarArray.append(progressBar)
    label = tk.Label(window, text="Progress: ")
    label.pack()
    labelArray.append(label)


def push():
    global yt
    yt = []
    for i in range(3):
        yt.append(pytube.YouTube(entryArray[i].get(), on_progress_callback=showProgress))
    for i in range(3):
        if checkVarArray[i].get() == 1:
            yt[i].streams[0].download()


button = tk.Button(text="download", command=push)
button.pack()

window.mainloop()