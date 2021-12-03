import random
import string
import json
from tkinter import *
from tkinter import messagebox

import pyperclip


# ---------Search-----------------------------------------------
def find_password():
    website = web_entry.get()
    if website == '':
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found")
        else:
            result = data.get(website)
            if result is None:
                messagebox.showinfo(title="Error", message="No details for the website exists")
            else:
                messagebox.showinfo(title=website, message=f'Email: {result.get("email")}\n'
                                                           f'Password: {result.get("password")}\n'
                                                           f'Your password has been copied in the clipboard')
                pyperclip.copy(result.get("password"))


# ---------Password Generator-----------------------------------


def generate_pass():
    password_generator_result = ''
    for i in range(18):
        password_generator = random.choice(
            [random.choice(string.ascii_letters),
             random.choice(string.digits),
             random.choice(string.punctuation)])
        if password_generator != "\\":
            password_generator_result = ''.join([password_generator_result, password_generator])
    pyperclip.copy(password_generator_result)
    pass_entry.delete(0, END)
    pass_entry.insert(END, password_generator_result)


# --------Save Password-----------------------------------------
def writing_in_json(_file, _data):
    with open(_file, "w") as _data_file:
        json.dump(_data, _data_file, indent=4)


def save_data():
    website = web_entry.get()
    email = mail_entry.get()
    password = pass_entry.get()
    new_data = {
        website.capitalize(): {
            "email": email,
            "password": password
        }
    }
    if website == '' or email == '' or password == '':
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        user_choice = messagebox.askokcancel(title=website,
                                             message=f"Your entries: \nEmail: {email} \n"
                                                     f"Password: {password} \nIf everything is alright press Ok")
        if user_choice:
            try:
                # Loading existing data
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                # Creates a json file to upload new_data
                writing_in_json("data.json", new_data)
            else:
                # updating data
                data.update(new_data)
                writing_in_json("data.json", data)
            finally:
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
web_entry.grid(row=1, column=1)

mail_entry = Entry(width=67)
mail_entry.insert(END, "myemailadress@mail.com")
mail_entry.grid(row=2, column=1, columnspan=2)

pass_entry = Entry(width=40)
pass_entry.grid(row=3, column=1)

# Buttons
search_btn = Button(text="Search", width=21, command=find_password)
search_btn.grid(row=1, column=2)

genpass_btn = Button(text="Generate Password", width=21, command=generate_pass)
genpass_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=57, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
