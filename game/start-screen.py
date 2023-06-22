import os
import json
import tkinter
from tkinter import messagebox


# API.json()['']['']

your_v = "0.4"

try:
    import requests
except ModuleNotFoundError :
    messagebox.showerror(title="Cat-Ball", message="you do not have requests")
    if (messagebox.askyesno(title="Cat-Ball", message="install requests", icon='error')):
        os.startfile("install-1.bat")
        quit()
API = requests.get("https://ogfishies2.github.io/Cat-Ball-API/start-screen-data.json")

try:
    import customtkinter
except ModuleNotFoundError :
    messagebox.showerror(title="Cat-Ball", message="you do not have customtkinter")
    if (messagebox.askyesno(title="Cat-Ball", message="install customtkinter", icon='error')):
        os.startfile("install-customtkinter.bat")
        quit()

API_login = requests.get("https://ogfishies2.github.io/Cat-Ball-API/User.json")


def start1():
    with open('login/test-acc.txt','r') as file:
        test_acc = file.read()
    if test_acc == "True":
        Username = "alt-acc"
        Password = "idk"
        dev = "False"
        print()
    if test_acc == "False":
        try:
            with open('login/acc/Username.txt','r') as file:
                Username = file.read()
            with open('login/acc/Password.txt','r') as file:
                Password = file.read()
            with open('login/acc/dev.txt','r') as file:
                dev = file.read()
        except FileNotFoundError:
            messagebox.showerror(title="Cat-Ball", message="you are not logined")
            os.startfile("login.py")
            quit()

    




    


    customtkinter.set_appearance_mode(API.json()['screen']['appearance_mode'])
    customtkinter.set_default_color_theme(API.json()['screen']['default_color_theme'])


    app = customtkinter.CTk()
    app.title(API.json()['screen']['title'])
    app.geometry(API.json()['screen']['geometry'])

    def start():
        os.startfile("game.py")
        quit()
    def LICENSE():
        os.startfile("LICENSE.url")
        quit()

    def Sign_out2():
        os.remove("login/acc/Username.txt")
        os.remove("login/acc/Password.txt")
        os.remove("login/acc/dev.txt")
        os.startfile("login.py")
        quit()

    buttonS = customtkinter.CTkButton(master=app, text="start", command=start)
    buttonS.pack(pady=10, padx=10)

    buttonL = customtkinter.CTkButton(master=app, text="LICENSE", command=LICENSE)
    buttonL.pack(pady=10, padx=10)
    
    frame_1 = customtkinter.CTkFrame(master=app)
    frame_1.pack(pady=20, padx=60, fill="both", expand=True)
    
    Usernametextonmainmenu = customtkinter.CTkLabel(master=frame_1,text=Username)
    Usernametextonmainmenu.pack()
    if test_acc == "False":
        buttonSn = customtkinter.CTkButton(master=frame_1,text="Sign out",command=Sign_out2)
        buttonSn.pack(pady=10, padx=10)
    

    app.mainloop()






if(API.json()['New-V']['ues'] == "yes"):
    if not(API.json()['New-V']['V'] == your_v):
        messagebox1 = f"new update {API.json()['New-V']['V']} you are on {your_v} "
        messagebox.showinfo(title="Cat-Ball", message=messagebox1)
        quit()
    elif(API.json()['New-V']['V'] == your_v):
        start1()
        
elif(API.json()['New-V']['ues'] == "no"):
    start1()