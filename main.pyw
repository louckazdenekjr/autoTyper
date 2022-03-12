import keyboard
import threading
import time
import tkinter

#----------------------------------------

typingBool = False
countdownTimer = ""

#----------------------------------------

def typeWrite(input):
    for char in input:
        keyboard.write(char)
        time.sleep(1/100)

def typeThreadFunc(window):
    global typingBool

    typingBool = True
    for i in range(5, -1, -1):
        countdownTimer = str(i)
        label1.config(text = countdownTimer)
        time.sleep(1)
        
    input = textInput.get()
    typeWrite(input)
    typingBool = False
    countdownTimer = ""
    label1.config(text = countdownTimer)

def runApp():
    def autoType(window):
        global typingBool

        if not typingBool:
            typingThread = threading.Thread (
                name = "typeThread",
                target = typeThreadFunc,
                args = (window)
            )
            
            typingThread.daemon = True
            typingThread.start()
            
    window = tkinter.Tk()
    window.geometry("600x200")
    window.resizable(False, False)
    window.configure(background = "gray20")
    window.title("autoTyper")
    window.option_add("*Font", "TkDefaultFont")

    label1 = tkinter.Label (
        window,
        text = countdownTimer,
        height = 2,
        background = "gray20", 
        foreground = "white"
    )

    button1 = tkinter.Button (
        text = "Type",
        height = 1,
        width = 20,
        background = "gray20",
        activebackground = "gray20",
        foreground = "white",
        activeforeground = "white",
        command = autoType(window)
    )

    button2 = tkinter.Button (
        text                = "Exit", 
        height              = 1, 
        width               = 20, 
        background          = "gray20", 
        activebackground    = "gray20", 
        foreground          = "white", 
        activeforeground    = "white", 
        command             = window.destroy
    )

    textInput = tkinter.Entry (
        window, 
        width       = 60, 
        background  = "gray60"
    )

    label1.place (
        relx    = 0.5, 
        rely    = 0.8, 
        anchor  = tkinter.CENTER
    )

    button1.place (
        relx = 0.2,
        rely = 0.8,
        anchor = tkinter.CENTER
    )

    button2.place (
        relx    = 0.8, 
        rely    = 0.8, 
        anchor  = tkinter.CENTER
    )

    textInput.place (
        relx    = 0.5, 
        rely    = 0.5, 
        anchor  = tkinter.CENTER
    )

    textInput.focus()

    tkinter.mainloop()
    
#----------------------------------------

if __name__ == "__main__":
    runApp()