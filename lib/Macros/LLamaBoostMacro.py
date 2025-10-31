#Imports
import tkinter as tk
import pyautogui
import json
import os

#Main Window
Main = tk.Tk()
Main.title("Boost Macro")
Main.geometry("500x300")
Main.resizable(False, False)

#Config
CONFIG_FILE = "config.json"

def save_config():
    config = {
        "StingerOn": StingerOn.get(),
        "GumOn": GumOn.get(),
        "JellyOn": JellyOn.get(),
        "CocoOn": CocoOn.get(),
        "CloudOn": CloudOn.get(),
        "GlitterOn": GlitterOn.get(),
        "SW": SW.get(),
        "SSlot": SSlot.get(),
        "GSlot": GSlot.get(),
        "JBSlot": JBSlot.get(),
        "CSlot": CSlot.get(),
        "CVSlot": CVSlot.get(),
        "GLSlot": GLSlot.get()
    }
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)
    print("Config saved.")


def load_config():
    if not os.path.exists(CONFIG_FILE):
        return
    with open(CONFIG_FILE, "r") as f:
        config = json.load(f)

    # Set checkbox states
    StingerOn.set(config.get("StingerOn", 0))
    GumOn.set(config.get("GumOn", 0))
    JellyOn.set(config.get("JellyOn", 0))
    CocoOn.set(config.get("CocoOn", 0))
    CloudOn.set(config.get("CloudOn", 0))
    GlitterOn.set(config.get("GlitterOn", 0))
    SW.set(config.get("SW", 0))

    # Set slot entries
    SSlot.delete(0, tk.END)
    SSlot.insert(0, config.get("SSlot", ""))
    GSlot.delete(0, tk.END)
    GSlot.insert(0, config.get("GSlot", ""))
    JBSlot.delete(0, tk.END)
    JBSlot.insert(0, config.get("JBSlot", ""))
    CSlot.delete(0, tk.END)
    CSlot.insert(0, config.get("CSlot", ""))
    CVSlot.delete(0, tk.END)
    CVSlot.insert(0, config.get("CVSlot", ""))
    GLSlot.delete(0, tk.END)
    GLSlot.insert(0, config.get("GLSlot", ""))

    print("Config loaded.")


#Macros
running = False

#Start Button
def start():
    global running
    if not running:
        running = True
        SCheckbox.configure(state="disabled")
        GCheckbox.configure(state="disabled")
        JBCheckbox.configure(state="disabled")
        CCheckbox.configure(state="disabled")
        CVCheckbox.configure(state="disabled")
        GLCheckbox.configure(state="disabled")
        SSlot.configure(state="disabled")
        GSlot.configure(state="disabled")
        JBSlot.configure(state="disabled")
        CSlot.configure(state="disabled")
        CVSlot.configure(state="disabled")
        GLSlot.configure(state="disabled")
        StartButton.configure(state="disabled")
        if SW.get():
            Main.after(2000)
        print("MACRO STARTED")
        stinger()
        gumdrop()
        jellybean()
        coconut()
        cloud()
        glitter()

#Stop button
def stop():
    global running
    running = False
    SCheckbox.configure(state="normal")
    GCheckbox.configure(state="normal")
    JBCheckbox.configure(state="normal")
    CCheckbox.configure(state="normal")
    CVCheckbox.configure(state="normal")
    GLCheckbox.configure(state="normal")
    SSlot.configure(state="normal")
    GSlot.configure(state="normal")
    JBSlot.configure(state="normal")
    CSlot.configure(state="normal")
    CVSlot.configure(state="normal")
    GLSlot.configure(state="normal")
    StartButton.configure(state="normal")
    print("MACRO STOPPED")

#Stingers
def stinger():
    if not running:
        return
    ss = SSlot.get()
    if running:
        if StingerOn.get():
            pyautogui.press(ss)
            print("STINGER ACTIVATED")
        Main.after(10000, stinger)

#Gumdrops
def gumdrop():
    if not running:
        return
    gs = GSlot.get()
    if running:
        if GumOn.get():
            pyautogui.press(gs)
            print("GUMDROP ACTIVATED")
        Main.after(2000, gumdrop)

#Jellybeans
def jellybean():
    if not running:
        return
    js = JBSlot.get()
    if running:
        if JellyOn.get():
            pyautogui.press(js)
            print("JELLYBEAN ACTIVATED")
        Main.after(30000, jellybean)

#Coconuts
def coconut():
    if not running:
        return
    cs = CSlot.get()
    if running:
        if CocoOn.get():
            pyautogui.press(cs)
            print("COCONUT ACTIVATED")
        Main.after(10000, coconut)

#Cloud Vials
def cloud():
    if not running:
        return
    cvs = CVSlot.get()
    if running:
        if CloudOn.get():
            pyautogui.press(cvs)
            print("CLOUD ACTIVATED")
        Main.after(60000, cloud)

#Glitter
def glitter():
    if not running:
        return
    gs = GSlot.get()
    if running:
        if GlitterOn.get():
            pyautogui.press(gs)
            print("GLITTER ACTIVATED")
        Main.after(150000, glitter)

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
StartWaitText = tk.Label(Main, text="Wait 2 seconds before start?")
StartWaitText.place(x=300, y=35)
HotkeyText = tk.Label(Main, text="Start F1 Stop F3")
HotkeyText.place(x=60, y=268)

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
SW = tk.IntVar()
StartWait = tk.Checkbutton(onvalue=1, offvalue=0, variable=SW)
StartWait.place(x=457, y=34)

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
StartButton = tk.Button(text="Start", command=start)
StartButton.place(x=200, y=265)
StopButton = tk.Button(text="Stop", command=stop)
StopButton.place(x=260, y=265)

#Save/Load Buttons
SaveButton = tk.Button(text="Save Config", command=save_config)
SaveButton.place(x=340, y=265)
LoadButton = tk.Button(text="Load Config", command=load_config)
LoadButton.place(x=420, y=265)


#Hotkeys
Main.bind("<F1>", lambda event: start())
Main.bind("<F3>", lambda event: stop())

#Loop
Main.mainloop()