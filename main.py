import random
import string
from tkinter import *
from tkinter import messagebox

import pyperclip


# ---------Password Generator-----------------------------------


def generate_pass():
    password_generator_result = ''
    for i in range(18):
        password_generator = random.choice(
            [random.choice(string.ascii_letters),
             random.choice(string.digits),
             random.choice(string.punctuation)])
        password_generator_result = ''.join([password_generator_result, password_generator])
    pyperclip.copy(password_generator_result)
    pass_entry.delete(0, END)
    pass_entry.insert(END, password_generator_result)


# --------Save Password-----------------------------------------

def save_data():
    website = web_entry.get()
    email = mail_entry.get()
    password = pass_entry.get()
    if website == '' or email == '' or password == '':
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        user_choice = messagebox.askokcancel(title=website,
                                             message=f"Your entries: \nEmail: {email} \n"
                                                     f"Password: {password} \nIf everything is alright press Ok")
        if user_choice:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                web_entry.delete(0, END)
                pass_entry.delete(0, END)
                web_entry.focus()


# -----------UI------------------------------------------------

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Labels
web_lbl = Label(text="Website:")
web_lbl.grid(row=1, column=0)

mail_lbl = Label(text="Email/Username:")
mail_lbl.grid(row=2, column=0)

pass_lbl = Label(text="Password:")
pass_lbl.grid(row=3, column=0)

# Entries
web_entry = Entry(width=40)
web_entry.focus()
web_entry.grid(row=1, column=1, columnspan=2)

mail_entry = Entry(width=40)
mail_entry.insert(END, "mail@mail.com")
mail_entry.grid(row=2, column=1, columnspan=2)

pass_entry = Entry(width=22)
pass_entry.grid(row=3, column=1)

# # Buttons
genpass_btn = Button(text="Generate Password", command=generate_pass)
genpass_btn.grid(row=3, column=2)
#
add_btn = Button(text="Add", width=34, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
