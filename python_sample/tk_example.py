from tkinter import ttk, messagebox
import tkinter

window = tkinter.Tk()

def check(text):
    for i in range(len(text)//2):
        if(text[i] != text[-i-1]):
            return False
    return True

def onClick():
    txt = entry.get()
    if(check(txt)):
        messagebox.showinfo("Result", "True")
    else:
        messagebox.showinfo("Result", "False")
    

entry = ttk.Entry(window, textvariable="entry")
button=tkinter.Button(window, text="OK", command=onClick)

entry.pack()
button.pack()
window.mainloop()
