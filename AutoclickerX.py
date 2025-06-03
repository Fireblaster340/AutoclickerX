import threading
from pynput.mouse import Button, Controller as MC
from pynput.keyboard import Key, Listener, Controller as KC
import tkinter as tk
from tkinter import simpledialog
from tkinter.messagebox import showinfo
import time 
import os
mouse = MC()
keyboard = KC()
running = False
Binding = False
DelayEntry = None
Keybind = None
InfoLabel = None
Start = None
BoundKey = "']'"
delay = 0.1
root = None
E = False
def Switch():
    global running
    time.sleep(0.3)
    os.system('clear')
    running = False if running == True else True


def Visual():
    global Start, DelayEntry, Keybind, InfoLabel, root, ReturnButton, BoundKey, Binding, listen, loop, listener
    Binding = False
    if root is None:
        root = tk.Tk()
        root.resizable(False, False)
        root.title("Free autoclicker!")
        root.geometry("500x400")
        root.bind("<Return>",lambda e:DelaySet(DelayEntry.get()))
    else:
        ReturnButton.place_forget()
    DelayEntry = tk.Entry(root,width=20)
    DelayEntry.place(x=162,y=90)
    Keybind = tk.Button(root, text="Change Keybind",height=2,width=15,command=KeybindWin)
    Keybind.place(x=170,y=250)
    InfoLabel = tk.Label(root,wraplength=350,text="Hi everyone! This is a free autoclicker I made for fun! Enter a time delay between clicks below and press enter! (Default keybinding for start/stop: ']')")
    InfoLabel.place(x=90,y=30)
    Start = tk.Button(root,height=3,width=20,text="Enter",command=lambda:DelaySet(DelayEntry.get()))
    Start.place(x=150,y=150)
    root.mainloop()
    listener.stop()
    BoundKey = None

def KeybindWin():
    global Start, DelayEntry, Keybind, InfoLabel, root, running, Binding, ReturnButton
    running = False
    DelayEntry.place_forget()
    Keybind.place_forget()
    InfoLabel.place_forget()
    Start.place_forget()
    Binding = True
    ReturnButton = tk.Button(root, text="Return", height=2, width=10, command=Visual)
    ReturnButton.place(x=20,y=300)
def DelaySet(NewDelay):
    global delay
    if simpledialog.askstring("...","...") == "E":
        SecretE()
        showinfo("...","Understood")
    if NewDelay == '':
        return None
    try:
        delay = float(NewDelay)
    except (ValueError,TypeError):
        return None

def OnKeyPress(Key):
    global BoundKey, Binding
    if not Binding:
        if str(Key) == BoundKey:
            Switch()
            return None
    else:
        showinfo(title="Keybinding",message="Keybind changed! New key: "+str(Key))
        BoundKey = str(Key)
def SecretE():
    global E
    E = True
def OnKeyRelease(Key):
    pass
def ClickLoop():
    global mouse, running, delay, BoundKey
    while BoundKey is not None:
        time.sleep(delay)
        if running:
            if not E:
                mouse.click(Button.left,1)
            else:
                keyboard.tap("e")
def Listen():
    global listener
    with Listener(on_press=OnKeyPress,on_release=OnKeyRelease) as listener:
        listener.join()
listen = threading.Thread(target=Listen,args=())
listen.start()
loop = threading.Thread(target=ClickLoop,args=())
loop.start()
Visual()
