from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]

    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    generated_password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, generated_password)

    pyperclip.copy(text=generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# with open("data.txt", mode="a") as data_file:
#     data = data_file.write("Amazon | commonemail@gmail.com | password \n")

with open("data.txt", mode="r") as data_file:
    data = data_file.read()


def add_data():
    site = website_input.get().title()
    email = email_username_input.get()
    password = password_input.get()
    error_message = None
    if not site:
        error_message = "Enter website"
    elif not email:
        error_message = "Enter an email"
    elif "@" not in email:
        error_message = "not a valid email"
    elif not password:
        error_message = "Enter a password"
    elif len(password) < 8:
        error_message = "Password must have minimum 8 characters"

    if error_message:
        messagebox.showerror(title="Invalid Info", message=error_message)
        return

    confirm = messagebox.askokcancel(title=site, message=f"Is this info correct:\n{site}\n{email}\n{password}")

    if not confirm:
        return

    formatted_data = f"{site} | {email} | {password} \n"
    mode = "w"
    if len(data) > 0:
        mode = "a"
    with open("data.txt", mode=mode) as current_data_file:
        current_data_file.write(formatted_data)

    website_input.delete(0, END)
    website_input.insert(0, "")

    password_input.delete(0, END)
    password_input.insert(0, "")

    messagebox.showinfo(title="Confirmation", message="Successfully added password")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("MyFastPass")
window.configure(padx=50, pady=50)

canvas = Canvas(master=window, height=200, width=200)
lock_image = PhotoImage(master=canvas, file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_name = Label(text="Website:")
website_name.grid(column=0, row=1)

email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_input = Entry(master=window, width=52)
website_input.grid(column=1, row=1, columnspan=2, sticky=W, padx=10)

email_username_input = Entry(master=window, width=52, )
email_username_input.grid(column=1, row=2, columnspan=2, sticky=W, padx=10)
email_username_input.insert(0, "commonemail@gmail.com")

password_input = Entry(master=window, width=31)
password_input.grid(column=1, row=3, sticky=W, padx=10)

generate_password_button = Button(master=window, text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky=W)

add_button = Button(master=window, text="Add", width=44, command=add_data)
add_button.grid(column=1, row=4, columnspan=2, sticky=W, padx=10)

website_input.focus_set()

window.mainloop()
