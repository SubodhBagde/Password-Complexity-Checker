from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import string
import pyperclip

def check_complexity():
    password = password_entry.get()
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    complexity = 0
    if length >= 8:
        complexity += 1
    if has_upper:
        complexity += 1
    if has_lower:
        complexity += 1
    if has_digit:
        complexity += 1
    if has_special:
        complexity += 1

    strength_meter["value"] = complexity * 20
    strength_meter["style"] = "TProgressbar" + str(complexity) + ".Horizontal"

    if complexity == 5:
        messagebox.showinfo("Password Complexity", "Very Strong")
    elif complexity == 4:
        messagebox.showinfo("Password Complexity", "Strong")
    elif complexity == 3:
        messagebox.showinfo("Password Complexity", "Moderate")
    elif complexity == 2:
        messagebox.showinfo("Password Complexity", "Weak")
    else:
        messagebox.showinfo("Password Complexity", "Very Weak")

def toggle_show_password():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

def clear_password():
    password_entry.delete(0, END)

def generate_password():
    password_length = random.randint(12, 16)
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

def copy_password():
    password = password_entry.get()
    pyperclip.copy(password)

# Create the main window
root = Tk()
root.title("Password Complexity Checker")
root.geometry("680x750")
root.configure(bg="#9FE2BF")

# Top frame
Label(root,text="Password Complexity Checker", width=2, font="Comicsansms 25 bold", fg="#0B5345", height=2, bg="#9FE2BF").pack(side=TOP, fill=X)

# Create a label and entry for password input
password_label = Label(root, text="Enter Password", font="Arial 20 bold", bg="#17A589")
password_label.pack(side="top", pady=20)
# password_label.place(x=650, y=100)
password_entry = Entry(root, show="*", font="Arial 18", bd=2, width=25)
password_entry.pack(side="top", pady=20)
# password_entry.place(x=585, y=150)

# Create a checkbox to show the password
show_password_var = BooleanVar()
show_password_checkbox = Checkbutton(root, text="Show Password", font="Arial 12", variable=show_password_var, command=toggle_show_password, bg="#52BE80")
show_password_checkbox.pack(side="top", pady=20)
# show_password_checkbox.place(x=950, y=150)

# Create a button to clear the password
clear_button = Button(root, text="Clear Password", font="Arial 12", bg="#52BE80", command=clear_password)
clear_button.pack(side="top", pady=20)
# clear_button.place(x=1100, y=150)

# Create a button to check password complexity
check_button = Button(root, text="Check Complexity", font="Arial 12", command=check_complexity, bg="#52BE80")
check_button.pack(side="top", pady=20)
# check_button.place(x=680, y=200)

# Create a progress bar for password strength meter
strength_label = Label(root, text="Password Strength", font="Arial 12 bold", bg="#17A589")
strength_label.pack(side="top", pady=20)
# strength_label.place(x=560, y=250)
strength_meter = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
strength_meter.pack(side="top", pady=20)
# strength_meter.place(x=735, y=250)

# Create buttons for generating and copying passwords
generate_button = Button(root, text="Generate Password", font="Arial 12", bg="#52BE80", command=generate_password, width=15, height=1)
generate_button.pack(side="top", pady=20)
# generate_button.place(x=670, y=300)
copy_button = Button(root, text="Copy Password",font="Arial 12", bg="#52BE80",  command=copy_password, width=15, height=1)
copy_button.pack(side="top", pady=20)
# copy_button.place(x=670, y=350)

# Start the Tkinter event loop
root.mainloop()
