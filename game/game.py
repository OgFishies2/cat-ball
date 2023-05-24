import os
from tkinter import messagebox
try:
    import requests
except:
    messagebox.showerror(title="Cat-Ball", message="you do not have requests")
    if (messagebox.askyesno(title="Cat-Ball", message="install requests", icon='error')):
        os.startfile("install-1.bat")

dev = False

with open('api-data-url.txt','r') as file:
    api_data_url = file.read()
API = requests.get(api_data_url)

hi = API.json()['Messages']['hi']
print(hi)


name = input("what is your name ")
if(name == "(DEV)"):
    if (messagebox.askyesno(title="Cat-Ball", message="Dev Mode", icon='warning')):
        dev = True
    else:
        dev = False
        name = "idk"
        
        
    
print(f"hi {name}")
if(dev):
    print(2)

q = int(input("what is 1+1="))


if(q == 2):
    print("yes")

if not(q == 2):
    print("no")

input()

