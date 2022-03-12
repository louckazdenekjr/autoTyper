import keyboard
import threading
import time
import tkinter
import sys

#----------------------------------------

typingBool = False
typingBoolLock = threading.Lock()
countdownTimer = ""

#----------------------------------------

def runApp():
    # define function to typewrite
    def typeWrite(input):
        for char in input:
            keyboard.write(char)
            time.sleep(1/100)

    # define thread target function
    def typeThreadFunc():
        global typingBool

        with typingBoolLock:
            typingBool = True
        
        for i in range(5, -1, -1):
            countdownTimer = str(i)
            label1.config(text = countdownTimer)
            time.sleep(1)
            
        input = textInput.get()
        typeWrite(input)
        
        with typingBoolLock:
            typingBool = False
        
        countdownTimer = ""
        label1.config(text = countdownTimer)
        
    # define main app function
    def autoType():
        global typingBool

        with typingBoolLock:
            if not typingBool:
                typingThread = threading.Thread (
                    name = "typeThread",
                    target = typeThreadFunc,
                )
                
                typingThread.daemon = True
                typingThread.start()
    
    # define app exit function
    def exitApp():
        window.destroy()
        sys.exit(0)
        
    # define app
    window = tkinter.Tk()
    window.geometry("600x200")
    window.resizable(False, False)
    background_color = "#1e1e1e"
    font_color = "#c8c8c8"
    window.configure(background = background_color)
    window.title("autoTyper")
    window.option_add("*Font", "TkDefaultFont")

    # define widgets
    label1 = tkinter.Label (
        window,
        text = countdownTimer,
        height = 2,
        background = background_color, 
        foreground = font_color
    )

    button1 = tkinter.Button (
        text = "Type",
        height = 1,
        width = 20,
        background = background_color,
        foreground = font_color,
        activebackground = background_color,
        activeforeground = font_color,
        command = autoType
    )

    button2 = tkinter.Button (
        text                = "Exit", 
        height              = 1, 
        width               = 20, 
        background          = background_color, 
        foreground          = font_color, 
        activebackground    = background_color, 
        activeforeground    = font_color, 
        command             = exitApp
    )

    textInput = tkinter.Entry (
        window, 
        width       = 60, 
        background  = "#bfbfbf"
    )

    # place widgets
    label1.place (
        relx    = 0.5, 
        rely    = 0.8, 
        anchor  = tkinter.CENTER
    )

    button1.place (
        relx = 0.25,
        rely = 0.8,
        anchor = tkinter.CENTER
    )

    button2.place (
        relx    = 0.75, 
        rely    = 0.8, 
        anchor  = tkinter.CENTER
    )

    textInput.place (
        relx    = 0.5, 
        rely    = 0.5, 
        anchor  = tkinter.CENTER
    )

    # focus main widget
    textInput.focus()

    # start event loop
    tkinter.mainloop()
    
#----------------------------------------

if __name__ == "__main__":
    runApp()