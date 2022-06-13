from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from string import ascii_letters, digits
from random import choice
import pyperclip
import json


class App(Tk):

    screen_width = 700
    screen_height = 400
    label_font = ('Arial', 14)
    password_size = 18

    def __init__(self):
        super().__init__()
        self.data = {}
        self.title('Password Manager')
        self.geometry(f'{self.screen_width}x{self.screen_height}')
        self.resizable(False, False)

        # Canvas
        self.canvas = Canvas(master=self)
        self.canvas.configure(
            width=self.screen_width,
            height=self.screen_height)
        self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Logo
        img = ImageTk.PhotoImage(image=Image.open('logo.png'))
        img_label = Label(master=self.canvas)
        img_label.image = img
        img_label.configure(image=img)
        img_label.grid(row=0, column=0, columnspan=4, sticky='ew')

        # Website Field
        website_label = Label(master=self.canvas)
        website_label.configure(text='Website:', font=self.label_font)
        website_label.grid(row=1, column=0)
        self.website_entry = Entry(master=self.canvas)
        self.website_entry.grid(row=1, column=1, columnspan=2, sticky='ew')

        # Username Field
        username_label = Label(master=self.canvas)
        username_label.configure(text='Email/Username:', font=self.label_font)
        username_label.grid(row=2, column=0)
        self.username_entry = Entry(master=self.canvas)
        self.username_entry.grid(row=2, column=1, columnspan=2, sticky='ew')

        # Password Field
        password_label = Label(master=self.canvas)
        password_label.configure(text='Password:', font=self.label_font)
        password_label.grid(row=3, column=0)
        self.password_entry = Entry(master=self.canvas)
        self.password_entry.grid(row=3, column=1, sticky='ew')

        # Password Button
        password_button = Button(master=self.canvas)
        password_button.configure(
            text='Generate Password',
            font=self.label_font,
            command=self.generate_password)
        password_button.grid(row=3, column=2, sticky='e')

        # Add Button
        add_button = Button(master=self.canvas)
        add_button.configure(
            text='Add',
            font=self.label_font,
            command=self.add_password)
        add_button.grid(row=4, column=1, columnspan=2, sticky='ew')

    def generate_password(self):
        characters = f'{ascii_letters}{digits}!@#$%^&*'
        password = []

        for _ in range(self.password_size):
            password.append(choice(characters))

        self.password_entry.delete(0, END)
        self.password_entry.insert(0, ''.join(password))
        pyperclip.copy("".join(password))
        messagebox.showinfo('Copied', 'Password saved to clipboard')

    def add_password(self):
        website = self.website_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not website or not username or not password:
            messagebox.showwarning(
                'Entry fields empty', 
                'All fields are required to save the password')
        else:
            is_ok = messagebox.askyesno('Confirm password save', f'Is it okay to save this password for {website}')
            if is_ok:
                if 'passwords' not in self.data.keys():
                    self.data['passwords'] = []
                
                with open('passwords.json', 'w') as f:
                    password_data = {
                        'website': website,
                        'username': username,
                        'password': password
                    } 
                    self.data['passwords'].append(password_data)
                    json.dump(self.data, f, indent=2)
                    f.close()
                
                messagebox.showinfo('Saved', 'Password saved to passwords.json')
                self.website_entry.delete(0, END)
                self.username_entry.delete(0, END)
                self.password_entry.delete(0, END)
            else:
                messagebox.showinfo('Not saved', 'Password not saved')

            
