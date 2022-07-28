from tkinter import *
from random import *
from tkinter import messagebox

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate():
    ls = []
    for _ in range(0, 4):
        ls.append(choice(letters))

    for _ in range(0, 4):
        ls.append((choice(numbers)))

    for _ in range(0, 4):
        ls.append(choice(symbols))
    shuffle(ls)
    st = ''.join(map(str, ls))
    pass_entry.insert(END, st)


def save():
    if web_entry.get() == "" or pass_entry.get() == "":
        messagebox.showerror("Error", "please don't leave any entry empty")
    else:
        ok = messagebox.askokcancel(title= web_entry.get(), message= f"These are the details entered:\n Email: {email_entry.get()}"
                                                                f"\n Password: {pass_entry.get()} \n I it ok to save?")
        if ok:
            with open("accounts.txt", mode="a") as file:
                file.write(f"{web_entry.get()} | {email_entry.get()} | {pass_entry.get()} \n")
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


window = Tk()
window.config(padx= 100, pady= 100)

image = PhotoImage(file= "logo.png")

canvas = Canvas(width= 200, height= 189)
canvas.create_image(100, 112, image = image)
canvas.grid(column= 2, row= 1)

web_label = Label(text= "Website")
web_label.grid(column= 1, row= 2)

web_entry = Entry(width= 45)
web_entry.grid(column= 2, row= 2, columnspan= 2)

email_label = Label(text= "Email/Username")
email_label.grid(column= 1, row= 3)

email_entry = Entry(width= 45)
email_entry.insert(END, "hantoli797@gmail.com")
email_entry.grid(column= 2, row= 3, columnspan= 2)

pass_label = Label(text= "Password:")
pass_label.grid(column= 1, row= 4)

pass_entry = Entry(width= 20)
pass_entry.grid(column= 2, row= 4)

gen_pass = Button(text= "Generate Password", width= 20, command= generate)
gen_pass.grid(column= 3, row= 4)

add = Button(text= "Add", width= 35, command= save)
add.grid(column= 2, row= 5, columnspan= 2)


window.mainloop()
