import os
from tkinter import messagebox
try:
    import requests
except:
    messagebox.showerror(title="Cat-Ball", message="you do not have requests")
    if (messagebox.askyesno(title="Cat-Ball", message="install requests", icon='error')):
        os.startfile("install-1.bat")

try:
    with open('login/Username.txt','r') as file:
        Username = file.read()
    with open('login/Password.txt','r') as file:
        Password = file.read()
    with open('login/dev.txt','r') as file:
         dev = file.read()
except FileNotFoundError:
    messagebox.showerror(title="Cat-Ball", message="you are not logined")

API = requests.get("https://ogfishies2.github.io/Cat-Ball-API/cat-bal-data.json")

print(f"hi {Username}")
if  input("play (y/n)") == "y" or "Y":
    pass
    

    



