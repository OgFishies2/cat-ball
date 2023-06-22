import requests
import customtkinter
from tkinter import messagebox
import os
API_login = requests.get("https://ogfishies2.github.io/Cat-Ball-API/User.json")

customtkinter.set_appearance_mode("Dark") #"System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")



def login2():
    
    def login1():
        try:
            User = f"{entry_1.get()}"
            Password = f"{entry_2.get()}"
            dev = API_login.json()[User]["dev"]
            if API_login.json()[User]["Username"] == User:
                if API_login.json()[User]["Password"] == Password:
                    with open('login/acc/Username.txt','w') as file:
                        file.write(User)
                    with open('login/acc/Password.txt','w') as file:
                        file.write(Password)
                    with open('login/acc/dev.txt','w') as file:
                        file.write(dev)
                    #os.startfile("Start-screen.py")
                    quit()
        except KeyError:
            messagebox.showerror(title="login error", message="Username or Password error")
            
    def login3():
        with open('login/test-acc.txt', 'w') as file:
            file.write("True")
            


    login = customtkinter.CTk()
    login.geometry("500,300")
    login.title("login")


    frame_1 = customtkinter.CTkFrame(master=login)
    frame_1.pack(pady=20, padx=60, fill="both", expand=True)

    label_1 = customtkinter.CTkLabel(master=frame_1, text="login",)
    label_1.pack(pady=12, padx=10)

    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Username")
    entry_1.pack(pady=12, padx=10)

    entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Password", show="*")
    entry_2.pack(pady=12, padx=10)


    button_1 = customtkinter.CTkButton(master=frame_1, command=login1, text="login")
    button_1.pack(pady=12, padx=10 )

    #button_2 = customtkinter.CTkButton(master=frame_1, command=login3, text="login to a test acc")
    #button_2.pack(pady=12, padx=10 )
    login.mainloop()


login2()

def pygame1():
    pass


