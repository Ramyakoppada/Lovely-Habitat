import tkinter as tk
from tkinter import ttk

def on_select(event):
    selected_item = combo.get()
    print(f"Selected: {selected_item}")

root = tk.Tk()
root.title("Dropdown Box Example")

items = ["breed", "Option 2", "Option 3", "Option 4"]

combo = ttk.Combobox(root, values=items)
combo.pack()
combo.set("Select an option")

combo.bind("<<ComboboxSelected>>", on_select)

root.mainloop()
