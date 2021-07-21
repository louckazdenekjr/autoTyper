import pyautogui
import time
import threading
import tkinter
from tkinter import mainloop, Label, ttk

typingBool=False
countdownTimer=""
autoTypeString=""

def type_thread(window):
    global typingBool
    global autoTypeString

    if not typingBool:
        typingBool=True
        for i in range(5, 0, -1):
            countdownTimer=str(i)
            label1.config(text=countdownTimer)
            time.sleep(1)

        countdownTimer="0"
        label1.config(text=countdownTimer)
        input = textInput.get("1.0","end-1c")
        pyautogui.write(input, interval=0.025)
        time.sleep(1)
        typingBool=False
        countdownTimer=""
        label1.config(text=countdownTimer)

    if typingBool:

        time.sleep(2)
    else:
        time.sleep(2)

def autoType():
    global typingBool
    global autoTypeString

    threading.Thread(target=type_thread, args=(window,), daemon=True).start()



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

textInput = tkinter.Text(window, height=1, width=60, wrap=tkinter.NONE, bg="gray60")
textInput.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

mainloop()


