import tkinter as tk
from tkinter import messagebox
import hashlib
import os

USER_FILE = 'users.txt'

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def user_exists(username):
    if not os.path.exists(USER_FILE):
        return False
    with open(USER_FILE, 'r') as file:
        for line in file:
            stored_username, _ = line.strip().split(',')
            if stored_username == username:
                return True
    return False

def register_user(username, password):
    if user_exists(username):
        return False, "Username already exists."
    hashed_password = hash_password(password)
    with open(USER_FILE, 'a') as file:
        file.write(f"{username},{hashed_password}\n")
    return True, "User registered successfully."

def authenticate_user(username, password):
    if not os.path.exists(USER_FILE):
        return False, "No users registered yet."
    with open(USER_FILE, 'r') as file:
        for line in file:
            stored_username, stored_hashed_password = line.strip().split(',')
            if stored_username == username and stored_hashed_password == hash_password(password):
                return True, "Login successful."
    return False, "Invalid username or password."

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("User System")
        self.geometry("1000x500")
        
        self.create_widgets()

    def create_widgets(self):
        self.lbl_title = tk.Label(self, text="Choose an option:")
        self.lbl_title.pack(pady=10)


        self.clear_widgets()
        self.lbl_title = tk.Label(self, text="Login")
        self.lbl_title.pack(pady=10)

        self.lbl_username = tk.Label(self, text="Username:")
        self.lbl_username.pack()
        self.ent_username = tk.Entry(self)
        self.ent_username.pack()

        self.lbl_password = tk.Label(self, text="Password:")
        self.lbl_password.pack()
        self.ent_password = tk.Entry(self, show="*")
        self.ent_password.pack()

        self.btn_submit = tk.Button(self, text="Submit", command=self.login)
        self.btn_submit.pack(pady=10)

        self.btn_back = tk.Button(self, text="Back", command=self.back_to_main)
        self.btn_back.pack(pady=5)

        self.btn_register = tk.Button(self, text="Register", command=self.show_register)
        self.btn_register.pack(pady=5)

    def show_register(self):
        self.clear_widgets()
        self.lbl_title = tk.Label(self, text="Register")
        self.lbl_title.pack(pady=10)

        self.lbl_username = tk.Label(self, text="Username:")
        self.lbl_username.pack()
        self.ent_username = tk.Entry(self)
        self.ent_username.pack()

        self.lbl_password = tk.Label(self, text="Password:")
        self.lbl_password.pack()
        self.ent_password = tk.Entry(self, show="*")
        self.ent_password.pack()

        self.btn_submit = tk.Button(self, text="Submit", command=self.register)
        self.btn_submit.pack(pady=10)

        self.btn_back = tk.Button(self, text="Back", command=self.back_to_main)
        self.btn_back.pack(pady=5)

    def register(self):
        username = self.ent_username.get()
        password = self.ent_password.get()
        success, message = register_user(username, password)
        messagebox.showinfo("Register", message)
        if success:
            self.back_to_main()

    def login(self):
        username = self.ent_username.get()
        password = self.ent_password.get()
        success, message = authenticate_user(username, password)
        messagebox.showinfo("Login", message)
        if success:
            self.back_to_main()

    def back_to_main(self):
        self.clear_widgets()
        self.create_widgets()

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
