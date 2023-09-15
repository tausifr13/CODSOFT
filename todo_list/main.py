from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle

root = Tk()
root.title('TODO - List')
root.geometry('500x300')

font_list = Font(
    family="Helvetica",
    size=30,
    weight="bold")

# FUNCTION

def delete_item():
    my_list.delete(ANCHOR)

def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

def task_done_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#dedede"
    )
    my_list.select_clear(0, END)

def undo_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#464646"
    )
    my_list.select_clear(0, END)

def delete_task_item():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "#dedede":
            my_list.delete(my_list.index(count))
        else:
            count += 1


def save_list():
    file_name = filedialog.asksaveasfilename(
        initialdir="C:/Codsoft", title="Save File", filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*"))
    )

    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'
        
        count = 0
        while count < my_list.size():
            if my_list.itemcget(count, "fg") == "#dedede":
                my_list.delete(my_list.index(count))
            else:
                count += 1

        stuff = my_list.get(0, END)

        output_file = open(file_name, 'wb')

        pickle.dump(stuff, output_file)

def open_list():
    file_name = filedialog.askopenfilename(
        initialdir="C:/Desktop/Codsoft", title="Open File", filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*"))
    )
    if file_name:
        my_list.delete(0, END)

        input_file = open(file_name, 'rb')

        stuff = pickle.load(input_file)

        for item in stuff:
            my_list.insert(END, item)

def delete_list():
    my_list.delete(0, END)


# Design

my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Save List", command=save_list)
file_menu.add_command(label="Open List", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear List", command=delete_list)


my_entry = Entry(root, font=Font, width=30, borderwidth=4)
my_entry.pack(padx=20, pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

delete_button = Button(button_frame, text="Delete Task", command=delete_item)
add_button = Button(button_frame, text="Add Task", command=add_item)
task_done_button = Button(button_frame, text="Task Done", command=task_done_item)
undo_task_button = Button(button_frame, text="Undo Task", command=undo_item)
delete_task_button = Button(button_frame, text="Delete Task Done", command=delete_task_item)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
task_done_button.grid(row=0, column=2)
undo_task_button.grid(row=0, column=3, padx=20)
delete_task_button.grid(row=0, column=4)


my_frame = Frame(root)
my_frame.pack(pady=10)

my_list = Listbox(my_frame, font=font_list, width=25, height=5, bg='SystemButtonFace',bd=0, fg="#464646", highlightthickness=0, selectbackground="#a6a6a6", activestyle="none")
my_list.pack(side=LEFT,fill=BOTH)


stuff = []
for item in stuff:
    my_list.insert(END, item)


# ScrollBar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT,fill=BOTH)

my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)



root.mainloop()