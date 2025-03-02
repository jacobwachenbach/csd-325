# Jacob Achenbach 3/2/2025

# App is a simple Todo list where you type a Todo item and click add item and if right clicked item it will delete item

import tkinter as tk
from tkinter import Menu, Scrollbar, Listbox, END

# Add task to the list function
def add_task():
    task = entry.get()
    if task:
        listbox.insert(END, task)
        entry.delete(0, END)

# Delete task on right-click function
def delete_task(event):
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)

# Function to exit application
def exit_app():
    root.destroy()

# Init main window
root = tk.Tk()
root.title("Achenbach-ToDo")
root.geometry("400x300")
root.configure(bg="#f4f4f4")  # Light gray background for a clean look

# Menu Bar
menu_bar = Menu(root)

# File Menu
file_menu = Menu(menu_bar, tearoff=0, bg="#ff9999", fg="black")  # Complementary color 1
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

# Label Instructions
instructions = tk.Label(root, text="Right-click a task to delete it.", fg="red", bg="#f4f4f4", font=("Arial", 10))
instructions.pack(pady=5)

# Adding tasks text input
entry = tk.Entry(root, width=40, bg="white", fg="black", font=("Arial", 10))
entry.pack(pady=5)

# Add tasks button
add_button = tk.Button(root, text="Add Task", command=add_task, bg="#99ccff", fg="black", font=("Arial", 10))
add_button.pack(pady=5)

# Container for listbox and scrollbar
frame = tk.Frame(root, bg="#f4f4f4")
frame.pack(pady=5)

# Scrollbar
scrollbar = Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# List tasks
listbox = Listbox(frame, width=50, height=10, yscrollcommand=scrollbar.set, bg="white", fg="black", font=("Arial", 10))
listbox.pack()

# Scrollbar
scrollbar.config(command=listbox.yview)

# Bind right-click to delete tasks
listbox.bind("<Button-3>", delete_task)

# Run the Tkinter event loop
root.mainloop()
