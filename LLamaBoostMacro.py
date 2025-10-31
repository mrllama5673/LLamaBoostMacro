#Imports
import tkinter as tk
import pyautogui

#Main Window
Main = tkinter.Tk()
Main.title("Boost Macro")
Main.geometry("500x300")
Main.resizable(False, False)

#Lables
Title = tk.Label(Main, text="LLama Boost Macro")
SText = tk.Label(Main, text="Stingers")
GText = tk.Label(Main, text="Gumdrops")
JBText = tk.Label(Main, text="Jelly Beans")
CText = tk.Label(Main, text="Coconuts")
CVText = tk.Label(Main, text="Cloud Vials")
GLText = tk.Label(Main, text="Glitter")
#Checkboxes
StingerOn = tk.IntVar()
SCheckbox = tk.Checkbutton(onvalue=1, offvalue=0, variable=StingerOn)
GumOn = tk.IntVar()
GCheckbox = tk.Checkbutton(onvalue=1, offvalue=0, variable=GumOn)
JellyOn = tk.IntVar()
JBCheckbox = tk.Checkbutton(onvalue=1, offvalue=0, variable=JellyOn)
CocoOn = tk.IntVar()
CCheckbox = tk.Checkbutton(onvalue=1, offvalue=0, variable=CocoOn)
CloudOn = tk.IntVar()
CVCheckbox = tk.Checkbutton(onvalue=1, offvalue=0, variable=CloudOn)
GlitterOn = tk.IntVar()
GLCheckbox = tk.Checkbutton(onvalue=1, offvalue=0, variable=GlitterOn)
#Hotbar Slots
SSlot = tk.Entry(width=2)
GSlot = tk.Entry(width=2)
JBSlot = tk.Entry(width=2)
CSlot = tk.Entry(width=2)
CVSlot = tk.Entry(width=2)
GLSlot = tk.Entry(width=2)
#Start/Stop
StartButton = tk.Button(text="Start", command='start')
StopButton = tk.Button(text="Stop", command=Main.quit)

#Placing Assets
Title.place(x=195, y=0)
SText.place(x=7, y=20)
GText.place(x=0, y=60)
JBText.place(x=2, y=100)
CText.place(x=1, y=140)
CVText.place(x=0, y=180)
GLText.place(x=10, y=220)
SCheckbox.place(x=20, y=40)
GCheckbox.place(x=20, y=80)
JBCheckbox.place(x=20, y=120)
CCheckbox.place(x=20, y=160)
CVCheckbox.place(x=20, y=200)
GLCheckbox.place(x=20, y=240)
SSlot.place(x=60, y=40)
GSlot.place(x=60, y=80)
JBSlot.place(x=60, y=120)
CSlot.place(x=60, y=160)
CVSlot.place(x=60, y=200)
GLSlot.place(x=60, y=240)
StartButton.place(x=200, y=265)
StopButton.place(x=260, y=265)

#Hotbar variables

#Macros
def boost():
    while(True):
        if SCheckbox.cget():
            SCheckbox.configure(state='Enabled')


Main.mainloop()