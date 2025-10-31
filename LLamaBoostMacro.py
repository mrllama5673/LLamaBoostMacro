#Imports
import tkinter as tk
import pyautogui

#Main Window
Main = tk.Tk()
Main.title("Boost Macro")
Main.geometry("500x300")
Main.resizable(False, False)

#Lables
Title = tk.Label(Main, text="LLama Boost Macro")
Title.place(x=195, y=0)

SText = tk.Label(Main, text="Stingers")
SText.place(x=7, y=20)

GText = tk.Label(Main, text="Gumdrops")
GText.place(x=0, y=60)

JBText = tk.Label(Main, text="Jelly Beans")
JBText.place(x=2, y=100)

CText = tk.Label(Main, text="Coconuts")
CText.place(x=1, y=140)

CVText = tk.Label(Main, text="Cloud Vials")
CVText.place(x=0, y=180)

GLText = tk.Label(Main, text="Glitter")
GLText.place(x=10, y=220)

#Checkboxes
StingerOn = tk.IntVar()
SCheckbox = tk.Checkbutton(onvalue=1, offvalue=0, variable=StingerOn)
SCheckbox.place(x=20, y=40)

GumOn = tk.IntVar()
GCheckbox = tk.Checkbutton(onvalue=1, offvalue=0, variable=GumOn)
GCheckbox.place(x=20, y=80)

JellyOn = tk.IntVar()
JBCheckbox = tk.Checkbutton(onvalue=1, offvalue=0, variable=JellyOn)
JBCheckbox.place(x=20, y=120)

CocoOn = tk.IntVar()
CCheckbox = tk.Checkbutton(onvalue=1, offvalue=0, variable=CocoOn)
CCheckbox.place(x=20, y=160)

CloudOn = tk.IntVar()
CVCheckbox = tk.Checkbutton(onvalue=1, offvalue=0, variable=CloudOn)
CVCheckbox.place(x=20, y=200)

GlitterOn = tk.IntVar()
GLCheckbox = tk.Checkbutton(onvalue=1, offvalue=0, variable=GlitterOn)
GLCheckbox.place(x=20, y=240)

#Hotbar Slots
SSlot = tk.Entry(width=2)
SSlot.place(x=60, y=40)

GSlot = tk.Entry(width=2)
GSlot.place(x=60, y=80)

JBSlot = tk.Entry(width=2)
JBSlot.place(x=60, y=120)

CSlot = tk.Entry(width=2)
CSlot.place(x=60, y=160)

CVSlot = tk.Entry(width=2)
CVSlot.place(x=60, y=200)

GLSlot = tk.Entry(width=2)
GLSlot.place(x=60, y=240)

#Start/Stop
StartButton = tk.Button(text="Start", command='start')
StartButton.place(x=200, y=265)

StopButton = tk.Button(text="Stop", command=Main.quit)
StopButton.place(x=260, y=265)

#Hotbar variables

#Macros
def boost():
    while(True):
        if StingerOn.get():
            pyautogui.press(int(SSlot.get()))


Main.mainloop()