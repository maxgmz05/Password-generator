import random
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Password generator")

#label that asks for password length
length_label = tk.Label(root,text='Enter the desired length for the password:')

#entry for length
length_entry = tk.Entry(root)

#label to choose what the password can contain
pw_contains_label = tk.Label(root, text='Choose what the password can contain:')

#checkbox vairables
upper_case_var = tk.IntVar()
#lower_case_var = tk.IntVar()
numbers_var = tk.IntVar()
symbols_var = tk.IntVar()

#checkboxes
upper_checkbox = tk.Checkbutton(root, text='Upper case letters (A-Z)', variable=upper_case_var)
#lower_checkbox = tk.Checkbutton(root, text='Lower case letters (a-z)', variable=lower_case_var)
numbers_checkbox = tk.Checkbutton(root, text='Numbers (0-9)', variable=numbers_var)
symbols_checkbox = tk.Checkbutton(root, text='Symbols (?!$%&*-)', variable=symbols_var)

#label to ask user if they want add anything extra
wantmore_label = tk.Label(root, text='Enter any extra characters \nyou may want in your password')

#entry for the extra characters
char_entry = tk.Entry(root)

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
customfont=("Courier", 25, "bold")
pw_display = tk.Label(root,text='',font=customfont)

#setting default value to the length entry widget
def restore_default(event):
    if length_entry.get == '':
        length_entry.insert(0,'8')
        
length_entry.insert(0,'8')
length_entry.bind("<FocusOut>", restore_default)

#function to work on button press

def password_generator_call():
    password_character_pool = ''+lowerc
    if upper_case_var.get():
        password_character_pool += upperc
    
    if numbers_var.get():
        password_character_pool += numberb
        
    if symbols_var.get():
        password_character_pool += symbol
        
    length_of_password = int(length_entry.get())
    
    password = password_generator(password_character_pool, length_of_password)
    
    pw_display.config(text=password)
    
#button to generate password

generate_button = tk.Button(root, text="Generate", command=password_generator_call)  
    
#function to generate password

def password_generator(pool,len=8):
    password = ''
    
    for i in range(len):
        password += random.choice(pool)
        
    print(password)
    return(password)

#function for when copy button is pressed

def copy_pass():
    root.clipboard_clear()
    pw = pw_display.cget('text')
    root.clipboard_append(pw)
    messagebox.showinfo("Copied","Password copied to clipboard!")

#button to copy password

copy_button = tk.Button(root, text='copy', command = copy_pass)

#creating space

root.rowconfigure(0, minsize=25)  
root.rowconfigure(1, minsize=35)  
root.rowconfigure(2, minsize=25)
root.rowconfigure(5, minsize=35)
root.rowconfigure(6, minsize=65)
root.rowconfigure(7, minsize=50)
root.rowconfigure(8, minsize=25)

#packing everything to the window

length_label.grid(row=0,column=0)
length_entry.grid(row=0,column=1, sticky='w')
pw_contains_label.grid(row=1,column=0, sticky='w')
upper_checkbox.grid(row=2,column=1, sticky='w')
numbers_checkbox.grid(row=3,column=1, sticky='w')
symbols_checkbox.grid(row=4,column=1, sticky='w')
wantmore_label.grid(row=5,column=0, sticky='w')
char_entry.grid(row=5,column=1, sticky='w')
pw_display.grid(row=6,column=0,columnspan=2)
generate_button.grid(row=7,column=0,columnspan=2)
copy_button.grid(row=8,column=0,columnspan=2)

#mainloop

root.mainloop()


