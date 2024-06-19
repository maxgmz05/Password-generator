import os
from pydoc import text
import sys
import tkinter as tk
from turtle import color
import random
from tkinter import messagebox

def load_asset(path):
    base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    assets = os.path.join(base, "assets")
    return os.path.join(assets, path)

window = tk.Tk()
window.geometry("499x602")
window.configure(bg="#000000")
window.title("")

#canvas

canvas = tk.Canvas(
    window,
    bg = "#000000",
    width = 499,
    height = 602,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x=0, y=0)

canvas.create_text(
    13,
    7,
    anchor="nw",
    text="Password Generator",
    fill="#ffffff",
    font=("Arial", 20 * -1)
)

entrytextcolor = "#FFFFFF"
entrybackcolor = "#343536"

#image assets
generate_button_image = tk.PhotoImage(file=load_asset("1.png"))
copy_button_image = tk.PhotoImage(file=load_asset("1.png"))
chkbutton_image = tk.PhotoImage(file=load_asset('2.png'))
button_3_image = tk.PhotoImage(file=load_asset("3.png"))
chekpressbutton = tk.PhotoImage(file=load_asset('4.png'))

#label that asks for password length
canvas.create_text(
    17,
    59,
    anchor="nw",
    text="Enter the number of \ncharacters",
    fill="#ffffff",
    font=("Arial", 20 * -1)
)

#entry for length
rect1_label = tk.Label(canvas, image= button_3_image, borderwidth=0)
rect1_label.place(x=249,y=51)

length_entry = tk.Entry(
    font=("Arial",24),
    fg=entrytextcolor,
    bd=0,
    bg=entrybackcolor,
    insertbackground="#000000",
    highlightthickness=0,
    justify="center"
)

length_entry.place(x=249, y=63, width=230, height=38,)

#label to choose what the password can contain
canvas.create_text(
    17,
    124,
    anchor="nw",
    text="The password can include :",
    fill="#ffffff",
    font=("Arial", 20 * -1)
)

#descriptions for the checkboxes
canvas.create_text(
    200,
    161,
    anchor="nw",
    text="Upper case (A-Z)",
    fill="#ffffff",
    font=("Arial", 20 * -1)
)

canvas.create_text(
    200,
    203,
    anchor="nw",
    text="Numbers (0-9)",
    fill="#ffffff",
    font=("Arial", 20 * -1)
)

canvas.create_text(
    200,
    247,
    anchor="nw",
    text="Symbols (?!$%&*-)",
    fill="#ffffff",
    font=("Arial", 20 * -1)
)

#checkbox variables
upper_case_var = tk.IntVar()
numbers_var = tk.IntVar()
symbols_var = tk.IntVar()

#checkboxes

#for upper case characters
upper_button = tk.Checkbutton(
    canvas,
    image= chkbutton_image,
    selectimage=chekpressbutton,
    indicatoron=0,
    borderwidth=0,
    bg='#000000',
    selectcolor="#000000",
    highlightthickness=0,
    activebackground="#000000",
    variable=upper_case_var
)

#for numbers
number_button = tk.Checkbutton(
    canvas,
    image= chkbutton_image,
    selectimage=chekpressbutton,
    indicatoron=0,
    borderwidth=0,
    bg="#000000",
    selectcolor="#000000",
    highlightthickness=0,
    activebackground="#000000",
    variable=numbers_var
)

#for symbols
symbo_button = tk.Checkbutton(
    canvas,
    image= chkbutton_image,
    selectimage=chekpressbutton,
    indicatoron=0,
    borderwidth=0,
    bg='#000000',
    selectcolor="#000000",
    activebackground="#000000",
    highlightthickness=0,
    variable=symbols_var
)

upper_button.place(x=143,y=163)
number_button.place(x=143,y=205)
symbo_button.place(x=143, y=247)

#label to ask user if they want add anything extra
canvas.create_text(
    17,
    317,
    anchor="nw",
    text="Any other characters you \nmay want in your \npassword",
    fill="#ffffff",
    font=("Arial", 20 * -1)
)

#entry for the extra characters
rect2_label = tk.Label(canvas, image= button_3_image, borderwidth=0)
rect2_label.place(x=249,y=308)

char_entry = tk.Entry(
    font=("Arial",24),
    fg=entrytextcolor,
    bd=0,
    bg=entrybackcolor,
    insertbackground="#000000",
    highlightthickness=0,
    justify="center"
)
char_entry.place(x=249, y=320, width=230, height=38)

#base variables
lowerc = list(range(97,123))
upperc = list(range(65,91))
number = list(range(48,58))
symbol = [63,33,36,37,38,42,45]

lowerc = ''.join(map(chr,lowerc))
upperc = ''.join(map(chr,upperc))
numberb = ''.join(map(chr,number))
symbol = ''.join(map(chr,symbol))

#label to display generated password
rect3_label = tk.Label(canvas, image= button_3_image, borderwidth=0)
rect3_label.place(x=249, y=441)

pw_display = tk.Entry(
    font=("courier",24,'bold'),
    fg=entrytextcolor,
    bd=0,
    bg=entrybackcolor,
    insertbackground="#000000",
    highlightthickness=0,
    justify="center"
)
pw_display.place(x=249, y=453, width=230, height=38,)
pw_display.insert(0, '********')

#setting default value to the length entry widget
def restore_default():
    if length_entry.get() == '':
        length_entry.insert(0,'8')

length_entry.insert(0,'8')

#function to call for password function
def password_generator_call():
    password_character_pool = ''+lowerc
    if upper_case_var.get():
        password_character_pool += upperc

    if numbers_var.get():
        password_character_pool += numberb

    if symbols_var.get():
        password_character_pool += symbol
        
    password_character_pool += char_entry.get()
    
    if length_entry.get()=='':
        length_entry.insert(0,'8')
        
    for i in length_entry.get():
        if ord(i) not in list(range(48,58)):
            print(i)
            length_entry.delete(0,'end')
            length_entry.insert(0,'8')  
            break

    length_of_password = int(length_entry.get())

    password = password_generator(password_character_pool, length_of_password)

    pw_display.delete(0,'end')
    pw_display.insert(0,password)

#button to generate password
generate_button = tk.Button(
    image=generate_button_image,
    relief="flat",
    borderwidth=0,
    background="#000000",
    bg="#000000",
    highlightthickness=0,
    activebackground="#000000",
    command=password_generator_call,
    text='Generate',
    font=("Arial",20 * -1),
    fg="#ffffff",
    compound="center"
)

generate_button.place(x=17, y=445, width=230, height=62)

#function to generate password
def password_generator(pool,len=8):
    password = ''
    
    for i in range(len):
        password += random.choice(pool)
        
    print(password)
    return(password)

#function for when copy button is pressed
def copy_pass():
    canvas.clipboard_clear()
    pw = pw_display.get()
    canvas.clipboard_append(pw)
    messagebox.showinfo("Copied","Password copied to clipboard!")

#button to copy password
copy_button = tk.Button(
    image=copy_button_image,
    relief="flat",
    borderwidth=0,
    background="#000000",
    highlightthickness=0,
    activebackground="#000000",
    command=copy_pass,
    text='Copy to clipboard',
    font=("Arial",20 * -1),
    fg="#ffffff",
    compound="center"
)

copy_button.place(x=147, y=531, width=230, height=62)

window.resizable(False, False)
window.mainloop()