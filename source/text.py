import tkinter as tk

def get_text():
    text = text_widget.get("1.0", "end-1c")  # Retrieve all text from line 1, character 0 to the end (excluding the final newline)
    print("Entered text:")
    print(text)

root = tk.Tk()
root.title("Multiline Text Entry Example")

text_widget = tk.Text(root, height=5, width=40)
text_widget.pack()

initial_text = """This is a multiline text entry field.
You can enter multiple lines of text here.
"""
text_widget.insert("1.0", initial_text)



root.mainloop()
