from tkinter import *
from PIL import ImageTk, Image


class App(Tk):

    screen_width = 700
    screen_height = 400
    label_font = ('Arial', 14)

    def __init__(self):
        super().__init__()
        self.title('Password Manager')
        self.geometry(f'{self.screen_width}x{self.screen_height}')
        self.resizable(False, False)

        # Canvas
        self.canvas = Canvas(master=self)
        self.canvas.configure(width=self.screen_width, height=self.screen_height)
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
        password_button.configure(text='Generate Password', font=self.label_font)
        password_button.grid(row=3, column=2, sticky='e')

        # Add Button
        add_button = Button(master=self.canvas)
        add_button.configure(text='Add', font=self.label_font)
        add_button.grid(row=4, column=1, columnspan=2, sticky='ew')
        

