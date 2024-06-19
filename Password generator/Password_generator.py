#new code
import os
from pydoc import text
import sys
import tkinter as tk
from turtle import color
import random

def clear_text():
    pw_display.delete(0, 'end')

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

generate_button_image = tk.PhotoImage(file=load_asset("1.png"))
button_3_image = tk.PhotoImage(file=load_asset("3.png"))

#creating 3 labels for text fields

rect1_label = tk.Label(canvas, image= button_3_image, borderwidth=0)
rect2_label = tk.Label(canvas, image= button_3_image, borderwidth=0)
rect3_label = tk.Label(canvas, image= button_3_image, borderwidth=0)

canvas.create_rectangle(0, 0, 499, 40, fill='#171717', outline="")

canvas.create_text(
    13,
    7,
    anchor="nw",
    text="Password Generator",
    fill="#ffffff",
    font=("Arial", 20 * -1)
)

rect1_label.place(x=249,y=51)

entrytextcolor = "#FFFFFF"
entrybackcolor = "#343536"

#entry for the number of characters

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

rect2_label.place(x=249,y=308)

#entry for additional characters to may be added to the generated password

char_entry = tk.Entry(
    font=("Arial",24),
    fg=entrytextcolor,
    bd=0,
    bg=entrybackcolor,
    insertbackground="#000000",
    highlightthickness=0,
    justify="center"
)

#base variables
lowerc = list(range(97,123))
upperc = list(range(65,91))
number = list(range(48,58))
symbol = [63,33,36,37,38,42,45]

lowerc = ''.join(map(chr,lowerc))
upperc = ''.join(map(chr,upperc))
numberb = ''.join(map(chr,number))
symbol = ''.join(map(chr,symbol))

#password output

pw_display = tk.Entry(
    font=("courier",24,'bold'),
    fg=entrytextcolor,
    bd=0,
    bg=entrybackcolor,
    insertbackground="#000000",
    highlightthickness=0,
    justify="center"
)

#setting default value to the length entry widget
def restore_default():
    if length_entry.get() == '':  # call get() as a method
        length_entry.insert(0,'8')

#function to generate password
def password_generator(pool,len=8):
    password = ''
    
    for i in range(len):
        password += random.choice(pool)
        
    print(password)
    return(password)

#function to work on button press
def password_generator_call():
    password_character_pool = ''+lowerc
    if upper_case_var.get():
        password_character_pool += upperc
    
    if numbers_var.get():
        password_character_pool += numberb
        
    if symbols_var.get():
        password_character_pool += symbol
        
    if length_entry.get()=='':
        length_entry.insert(0,'8')
        
    length_of_password = int(length_entry.get())
    
    password = password_generator(password_character_pool, length_of_password)
    
    pw_display.delete(0,'end')
    pw_display.insert(0, password)
    
pw_display.place(x=249, y=453, width=230, height=38,)

char_entry.place(x=249, y=320, width=230, height=38,)

pw_display.insert(0, '********')

canvas.create_text(
    17,
    59,
    anchor="nw",
    text="Enter the number of \ncharacters",
    fill="#ffffff",
    font=("Arial", 20 * -1)
)

canvas.create_text(
    17,
    124,
    anchor="nw",
    text="The password can include :",
    fill="#ffffff",
    font=("Arial", 20 * -1)
)

#checkbottens for characters that can be included

chkbutton_image = tk.PhotoImage(file=load_asset('2.png'))
chekpressbutton = tk.PhotoImage(file=load_asset('4.png'))

#variables for checkbuttons
upper_case_var = tk.IntVar()
numbers_var = tk.IntVar()
symbols_var = tk.IntVar()

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

canvas.create_text(
    17,
    317,
    anchor="nw",
    text="Any other characters you \nmay want in your \npassword",
    fill="#ffffff",
    font=("Arial", 20 * -1)
)

#generate button

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

canvas.create_text(
    249,
    403,
    anchor="nw",
    text="Your password:",
    fill="#ffffff",
    font=("Arial", 20 * -1)
)

rect3_label.place(x=249, y=441)

canvas.create_text(
    249,
    454,
    anchor="nw",
    text="**************",
    fill="#ffffff",
    font=("Arial", 15 * -1)
)

canvas.create_text(
    17,
    460,
    anchor="nw",
    text="Generate",
    fill="#ffffff",
    font=("Arial", 20 * -1)
)

#copy button

copy_button_image = tk.PhotoImage(file=load_asset("1.png"))

copy_button = tk.Button(
    image=copy_button_image,
    relief="flat",
    borderwidth=0,
    background="#000000",
    highlightthickness=0,
    activebackground="#000000",
    command=clear_text,
    text='Copy to clipboard',
    font=("Arial",20 * -1),
    fg="#ffffff",
    compound="center"
)

copy_button.place(x=147, y=531, width=230, height=62)

canvas.create_text(
    147,
    546,
    anchor="nw",
    text="Copy to clipboard",
    fill="#ffffff",
    font=("Arial", 20 * -1)
)

window.resizable(False, False)
window.mainloop()
