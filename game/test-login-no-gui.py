import requests
import os
from tkinter import messagebox

API_login = requests.get("https://ogfishies2.github.io/Cat-Ball-API/User.json")

while True:
    print("login")
    Username = input("Username: ")
    Password = input("Password: ")

    try:
        API_login.json()[Username]["Username"]
        API_login.json()[Username]["Password"]
        quit()
    except:
        messagebox.showerror(title="login", message="error")

