import os
import tkinter
from tkinter import messagebox

try:
    import requests
except:
    messagebox.showerror(title="Cat-Ball", message="you do not have requests")
    if (messagebox.askyesno(title="Cat-Ball", message="install requests", icon='error')):
        os.startfile("install-1.bat")
        quit()

try:
    import customtkinter
except:
    messagebox.showerror(title="Cat-Ball", message="you do not have customtkinter")
    if (messagebox.askyesno(title="Cat-Ball", message="install customtkinter", icon='error')):
        os.startfile("install-customtkinter.bat")
        quit()
    
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x240")

def start():
    os.startfile("game.py")
    quit()
def LICENSE():
    os.startfile("LICENSE.py")

buttonS = customtkinter.CTkButton(master=app, text="start", command=start)
buttonS.pack()

buttonL = customtkinter.CTkButton(master=app, text="LICENSE", command=LICENSE)
buttonL.pack()

app.mainloop()