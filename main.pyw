import keyboard
import time
import threading
import tkinter
from tkinter import mainloop, Label, ttk

typingBool=False
countdownTimer=""

def typeWrite(input):
    for char in input:
        keyboard.write(char)
        time.sleep(1/100)

def type_thread(window):
    global typingBool

    typingBool=True
    for i in range(5, -1, -1):
        countdownTimer=str(i)
        label1.config(text=countdownTimer)
        time.sleep(1)
    input = textInput.get()
    typeWrite(input)
    typingBool=False
    countdownTimer=""
    label1.config(text=countdownTimer)

def autoType():
    global typingBool

    if not typingBool:
        threading.Thread(target=type_thread, args=(window,)).start()

window = tkinter.Tk()
window.geometry("600x200")
window.resizable(0, 0)
window.configure(bg='gray20')
window.title("autoTyper")
window.option_add("*Font", "TkDefaultFont")

button1 = tkinter.Button(text="Type", height=1, width=20, background = "gray20", activebackground = "gray20", foreground="white", activeforeground="white", command = autoType)
button1.place(relx=0.2, rely=0.8, anchor=tkinter.CENTER)

label1 = tkinter.Label(window, text=countdownTimer, height=2, background = "gray20", foreground="white")
label1.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

button2 = tkinter.Button(text="Exit", height=1, width=20, background = "gray20", activebackground = "gray20", foreground="white", activeforeground="white", command = window.destroy)
button2.place(relx=0.8, rely=0.8, anchor=tkinter.CENTER)

textInput = tkinter.Entry(window, width=60, bg="gray60")
textInput.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
textInput.focus()

mainloop()
