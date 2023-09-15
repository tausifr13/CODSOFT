from tkinter import *
import string
import random
import pyperclip


# FUNCTION
def generator():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    all = small_alphabets + capital_alphabets + numbers + special_characters
    password_length = int(length_Box.get())
    pdField.delete(0, END)

    if choice.get() == 1:
        pdField.insert(0, random.sample(small_alphabets + capital_alphabets + numbers, password_length))

    if choice.get() == 2:
        pdField.insert(0, random.sample(all, password_length))


def copy():
    random_password = pdField.get()
    pyperclip.copy(random_password)


root = Tk()
root.title('Password Generator')
root.config(bg='gray20')
#root.geometry("500x350")

choice = IntVar()
Font = ('arial', 13, 'bold')
pdLabel = Label(root, text='Password Generator',font=('times new romen',20,'bold'), bg='gray20', fg='white',justify=CENTER)
pdLabel.grid(pady=10)

# ------ Choice Button -----

type = Label(root, text='Type of Password', font=Font, bg='gray20', fg='white')
type.grid(pady=3)

button_choice = Frame(root)
button_choice.grid(pady=20)


mediumButton = Radiobutton(button_choice, text='Medium', value = 1, variable = choice, font = Font)
mediumButton.grid(row=0, column=1)

strongButton = Radiobutton(button_choice, text='Strong', value = 2, variable = choice, font = Font)
strongButton.grid(row=0, column=2)



lengthLabel = Label(root, text='Password Length', font=Font, bg='gray20', fg='white')
lengthLabel.grid(pady=5)

length_Box = Spinbox(root, from_=5, to=18, width=5, font=Font)
length_Box.grid(pady=5)

generateButton = Button(root, text='Generate', font=Font, command=generator)
generateButton.grid(pady=5)

pdField = Entry(root, width=45, bd=2, font=Font)
pdField.grid()


# Copy the Password
copyButton = Button(root, text='Copy', font=Font, command=copy)
copyButton.grid(pady=5)



root.mainloop()