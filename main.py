from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- FIND PASS FUNCTION ------------------------------- #
def find_password():
    website = entry_website.get().title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            email = data[website]["email"]
            password = data[website]["password"]
    except KeyError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email_uname.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

# Labels
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)
label_email_uname = Label(text="Email/Username:")
label_email_uname.grid(column=0, row=2)
label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

# Entries
entry_website = Entry()
entry_website.grid(column=1, row=1, sticky="EW")
entry_website.focus()
entry_email_uname = Entry()
entry_email_uname.grid(column=1, row=2, columnspan=2, sticky="EW")
entry_email_uname.insert(0, "andremessias.az@gmail.com")
entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="EW")

# Buttons
generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3, sticky="EW")
add_btn = Button(text="Add", width=35, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")
search_btn = Button(text="Search", command=find_password)
search_btn.grid(column=2, row=1, columnspan=2, sticky="EW")

mainloop()
