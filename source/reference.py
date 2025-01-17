import mysql.connector 
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
from tkinter import Label, PhotoImage, Button, Canvas

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '2004',

)
cursor = conn.cursor()
cursor.execute('create database if not exists upload')

cursor.execute('use upload')

# Tkinter application
class ImageStorageApp:
    def _init_(self, master):
        self.master = master
        self.master.title("Image Storage App")

        # UI elements
        self.login_frame = Frame(self.master, bg='#e6e6fa')  # Set background color
        self.login_frame.pack(expand=True, fill='both')  # Expand and fill the frame to cover the whole window
    
        self.label = Label(self.login_frame, text="Select an image:")
        self.label.pack(pady=20)
        #self.label.place(x = 400, y = 400)

        # self.name_lbl = Label(self.frame, text= 'image name', bg = 'white', fg = 'steelblue', anchor='w').place(x = 20, y = 50)
        # self.name_entry = Entry(self.frame, width= 15)

        self.select_button = Button(self.login_frame, text="Select Image", command=self.select_image)
        self.select_button.pack(pady=20)
        #self.select_button.place(x = 400, y = 600)

        self.save_button = Button(self.login_frame, text="Save Image", command=self.save_image)
        self.save_button.pack(pady=20)
        #self.save_button.place(x = 400, y = 800)


    def select_image(self):
        file_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", ".png;.jpg;*.jpeg")])
        if file_path:
            self.display_selected_image(file_path)

    def display_selected_image(self, file_path):
        image = Image.open(file_path)
        image = image.resize((200, 200))  # Resize the image for display
        photo = ImageTk.PhotoImage(image)

        self.label.config(image=photo)
        self.label.image = photo
        self.selected_image_path = file_path

        
    def save_image(self):
        if hasattr(self, 'selected_image_path'):
            with open(self.selected_image_path, 'rb') as image_file:
                image_data = image_file.read()

            image_name = self.selected_image_path.split('/')[-1]  # Extract the image name

        try:
            # Using parameterized query to insert image data
            query = "INSERT INTO images (name, image) VALUES (%s, %s)"
            cursor.execute(query, (image_name, image_data))
            conn.commit()
            print("Image saved to the database.")

            cursor.execute("SELECT name, image FROM images")
            self.images = cursor.fetchall()
            self.current_image_index = 0

            if self.images:
                self.ImagedisplayApp()
        
        except mysql.connector.Error as e:
            print(f"Error: {e}")


# Tkinter application

    def ImagedisplayApp(self):
        self.login_frame.destroy()
       # self.master = master
        self.master.title("Image Display App")

        # UI elements
        self.canvas = Canvas(self.master)
        self.canvas.pack()

        self.next_button = Button(self.master, text="Next Image", command=self.next_image)
        self.next_button.pack()

        # Retrieve all images from the database
        cursor.execute("SELECT name, image FROM images")
        self.images = cursor.fetchall()
        self.current_image_index = 0

        if self.images:
            self.display_image()

    def display_image(self):
        try:
            image_name, image_data = self.images[self.current_image_index]

            # Create a temporary image file and display it using Tkinter
            with open(image_name, 'wb') as img_file:
                img_file.write(image_data)

            # Resize the image for display
            image = Image.open(image_name)
            image = image.resize((400, 400))  # Use Image.ANTIALIAS
            photo = ImageTk.PhotoImage(image)

            self.canvas.config(width=image.width, height=image.height)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.canvas.image = photo

        except Exception as e:
            print(f"Error displaying image: {e}")

    def next_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.images)
        self.display_image()

# Create Tkinter window

# Close the database connection when the Tkinter window is closed


# Create Tkinter window
root = Tk()

root.geometry('550x350+550+200')
root.resizable(True, True)
app = ImageStorageApp(root)
root.mainloop()

# Close the database connection when the Tkinter window is closed