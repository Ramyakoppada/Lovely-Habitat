import tkinter as tk
from tkinter import Tk, Frame, Label, Entry, Button, messagebox, ttk
import mysql.connector
from tkinter import *
import webbrowser
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import Label, PhotoImage, Button, Canvas
import re


conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Asri@21',

)
cursor = conn.cursor()
cursor.execute('create database if not exists LOVELYHABITAT')

cursor.execute('use LOVELYHABITAT')


#from PIL import Image, ImageTk
fonts = ('Times Of New Roman', 16, 'bold')
user = 'Krishna'
passw = '1234'



class Login:
    def __init__(self, root):
        self.root = root
    
        self.loginn_frame = Frame(self.root, width = 2000, height = 2000, bg = '#404040')
        self.loginn_frame.place(x = 0, y = 0)
        

        self.login_frame = Frame(self.root, width = 1400, height = 650, bg = 'white')
        self.login_frame.place(x = 70, y = 70)

        self.img = PhotoImage(file='mainpup.png')
        self.label_image = Label(self.login_frame, image=self.img, border=5, bg='white')
        self.label_image.place(x=2, y=12)

        self.label = tk.Label(self.root)
        img = Image.open(r"C:/Users/priya/Desktop/pythonproject/source/Add a heading (2).png")
        img = img.resize((400, 485))
        self.label.img = ImageTk.PhotoImage(img)
        self.label['image'] = self.label.img

        self.label.place(x = 1000, y = 150)
        
        self.user_name_entry = Entry(self.label, width  = 25, font = fonts, bg = '#dbbfd8')
        self.user_name_entry.place(x = 55, y = 95)

        self.user_pass_entry = Entry(self.label, width  = 25, font = fonts, bg = '#dbbfd8', show = "*")
        self.user_pass_entry.place(x = 55, y = 190)

        self.submit_btn = Button(self.label, text = 'LOGIN', bg = '#404040', fg = 'white', font = fonts, command = self.check_login, cursor = 'hand2', activebackground = 'blue')
        self.submit_btn.place(x = 167, y = 280)

        self.submit_btn = Button(self.label, text = 'SIGN_UP', bg = '#404040', fg = 'white', font = fonts, command = self.acnt_signup, cursor = 'hand2', activebackground = 'blue')
        self.submit_btn.place(x = 155, y = 360)

    def acnt_signup(self):

        self.label.destroy()

        self.label1 = tk.Label(self.root)
        img = Image.open(r"C:/Users/priya/Desktop/pythonproject/source/Add a heading (8).png")
        img = img.resize((527, 525))
        self.label1.img = ImageTk.PhotoImage(img)
        self.label1['image'] = self.label1.img

        self.label1.place(x = 900, y = 135)

        self.set_user_name_entry = Entry(self.label1, width  = 20, font = fonts, bg = '#dbbfd8')
        self.set_user_name_entry.place(x = 248, y = 70)

        self.set_mobile_entry= Entry(self.label1, width  = 20, font = fonts, bg = '#dbbfd8')
        self.set_mobile_entry.place(x = 248, y = 130)

        self.set_mail_entry = Entry(self.label1, width  = 20, font = fonts, bg = '#dbbfd8')
        self.set_mail_entry.place(x = 248, y = 190)

        self.set_pass_entry = Entry(self.label1, width  = 20, font = fonts, bg = '#dbbfd8')
        self.set_pass_entry.place(x = 248, y = 250)

        self.set_pass_entry_cnf = Entry(self.label1, width  = 20, font = fonts, bg = '#dbbfd8')
        self.set_pass_entry_cnf.place(x = 248, y = 310)

        

        self.submit_btn = Button(self.label1, text = 'SUBMIT', bg = '#404040', fg = 'white', font = fonts, cursor = 'hand2', activebackground = 'blue', command =self.save_data)
        self.submit_btn.place(x = 220, y = 420)

    def save_data(self)-> None:
        self.uname = self.set_user_name_entry.get()
        self.mbno =  self.set_mobile_entry.get()
        self.umail = self.set_mail_entry.get()
        self.upass = self.set_pass_entry.get()
        self.ucpass = self.set_pass_entry_cnf.get()

        cursor.execute(f"SELECT * FROM user_details WHERE username = '{self.uname}'")
        self.data = cursor.fetchall()
        self.data = [data[0] for data in self.data]

        if re.match(r'^[a-zA-Z0-9._%+-]+@gmail\.com$', self.umail):
            if re.match(r'^[6-9]\d{9}$', self.mbno):
                if self.upass == self.ucpass and len(self.data) == 0:
                    self.query = f"insert into user_details values('{self.uname}',{self.mbno},'{self.umail}','{self.upass}')"
                    cursor.execute(self.query)
                    conn.commit()
                    messagebox.showinfo('SAVED','SUCCESSFULLY SIGNED UP')

                    self.label1.destroy()
                    dashboard = Dashboard(self.root)
                elif len(self.data) != 0:
                    messagebox.showinfo('error','username already exists')
                elif self.upass != self.ucpass:
                    messagebox.showinfo('error','password reentered is not same as pass')
            
            else:
                messagebox.showinfo('Validation Result', 'Invalid Mobile Number!')

        else:
            messagebox.showinfo('Validation Result', 'Invalid gmail Address!')

    def check_login(self):
        self.name = self.user_name_entry.get()
        self.password = self.user_pass_entry.get()
        if self.name.strip() == "" or self.password.strip() == "":
            messagebox.showerror('EMPTY','Please enter your login details')
            return

        cursor.execute(f"SELECT * FROM user_details WHERE username = '{self.name}'")
        self.data = cursor.fetchall()
        self.data = [data[0] for data in self.data]
        self.fdata = ''.join(self.data)

        cursor.execute(f"SELECT * FROM user_details WHERE username = '{self.name}'")
        self.pass_data = cursor.fetchall()
        self.pass_data = [data[3] for data in self.pass_data]
        self.fpass_data = ''.join(self.pass_data)

        if self.name == self.fdata:
            if self.password == self.fpass_data:
                messagebox.showinfo('WELCOME','WELCOME TO PET WORLD')
                self.label.destroy()
                dashboard = Dashboard(self.root)
            else:
                messagebox.showerror('WRONG PASSWORD','CHECK YOUR PASSWORD')
        else:
            messagebox.showerror('WRONG ID','INVALID USERNAME')
        
class Dashboard:
    def __init__(self, root):
        self.root = root


        self.login11 = Frame(self.root, width = 2000, height = 2000, bg = '#9c9cb5')
        self.login11.place(x = 265, y = 0)

        self.homepage = tk.Label(self.login11)
        img = Image.open(r"C:/Users/priya/Desktop/pythonproject/source/homepageimg.jpg")
        img = img.resize((1275, 800))
        self.homepage.img = ImageTk.PhotoImage(img)
        self.homepage['image'] = self.homepage.img
        self.homepage.place(x = 265, y = 0)

        root.title("Adopt pets don't shop")
       
        # self.login1 = Frame(self.root, width = 2000, height = 2000, bg = 'white')
        # self.login1.place(x = 0, y = 0)

        # self.homepage = tk.Label(self.login1)
        # img = Image.open(r"C:/Users/priya/Desktop/pythonproject/source/homepageimg.jpg")
        # img = img.resize((1275, 800))
        # self.homepage.img = ImageTk.PhotoImage(img)
        # self.homepage['image'] = self.homepage.img
        # self.homepage.place(x = 265, y = 0)

        # self.root.title('WELCOME TO THE PET FAMILY')

        # submit_btn10 = Button(self.root, text = 'LOGOUT', bg = '#dbbfd8', fg = '#404040', font = fonts, command = self.visit_again, cursor = 'hand2', activebackground = 'blue')
        # submit_btn10.place(x = 1400, y = 13)

        user_name2 = Label(self.root, text = '', font = fonts, bg = '#404040', fg = '#e6e6fa', width = 20, height=150)
        user_name2.place(x = 0, y = 0)

        btn = Button(self.root, text = 'HOME', bg = '#404040',relief=tk.FLAT, fg = '#e6e6fa', font = fonts, cursor = 'hand2',command=self.funhomepage, activebackground = '#FFA500',width=19) 
        btn.place(x = -1, y=100)

        btn1 = Button(self.root, text = 'BUYER', bg = '#404040',relief=tk.FLAT, fg = '#e6e6fa', font = fonts, cursor = 'hand2',command = self.buyerclass, activebackground = '#FFA500',width=19) 
        btn1.place(x = 0, y=200)

        btn2 = Button(self.root, text = 'SELLER', bg = '#404040', relief=tk.FLAT,fg = '#e6e6fa', font = fonts, command=self.sellerclass, cursor = 'hand2', activebackground = '#FFA500',width=19) 
        btn2.place(x = 0, y=300)

        btn3 = Button(self.root, text = 'ABOUT CARE', bg = '#404040', relief=tk.FLAT,fg = '#e6e6fa', font = fonts, command=self.careclass , cursor = 'hand2', activebackground = '#FFA500',width=19) 
        btn3.place(x = 0, y=400)

        btn4 = Button(self.root, text = 'NEARBY LOCATIONS', bg = '#404040',relief=tk.FLAT, fg = '#e6e6fa', font = fonts,command = self.feeding ,cursor = 'hand2', activebackground = '#FFA500',width=19) 
        btn4.place(x = 0, y=500)

        btn5 = Button(self.root, text = 'LOGOUT', bg = '#404040',relief=tk.FLAT, fg = '#e6e6fa', font = fonts ,command=self.visit_again, cursor = 'hand2', activebackground = '#FFA500',width=19) 
        btn5.place(x = 0, y=600)
        
        self.login2 = Frame(self.root, width = 2000, height = 2000, bg = '#9c9cb5')
        self.login2.place(x = 225, y = 0)

        self.img1 = PhotoImage(file='mainnpup.png')
        self.label_image1 = Label(self.login2, image=self.img1, border=0,bg = "#9c9cb5")
        self.label_image1.place(x=225, y=0)

    def feeding(self):
        self.petscare.destroy()
        self.login9.destroy()

        self.login12 = Frame(self.root, width = 2000, height = 2000, bg = '#e6e6fa')
        self.login12.place(x = 265, y = 0)

        self.petfood = tk.Label(self.root)
        img = Image.open(r"C:/Users/priya/Desktop/pythonproject/source/petfood.jpg")
        img = img.resize((350, 400))
        self.petfood.img = ImageTk.PhotoImage(img)
        self.petfood['image'] = self.petfood.img
        self.petfood.place(x = 330, y = 200)
        def open_web_browser(event):
            webbrowser.open_new("http://surl.li/rbjym")  # Replace "https://example.com" with your desired URL
        self.petfood.bind('<Button-1>', open_web_browser)

        self.petgroom = tk.Label(self.root)
        img = Image.open(r"C:/Users/priya/Desktop/pythonproject/petcare.jpg")
        img = img.resize((350, 400))
        self.petgroom.img = ImageTk.PhotoImage(img)
        self.petgroom['image'] = self.petgroom.img
        self.petgroom.place(x = 720, y = 200)

        def open_web_browser(event):
            webbrowser.open_new("http://surl.li/rbkig")  # Replace "https://example.com" with your desired URL

# Bind the function to the image label
        self.petgroom.bind('<Button-1>', open_web_browser)

        self.petcare = tk.Label(self.root)
        img = Image.open(r"C:/Users/priya/Desktop/pythonproject/source/pethosp.jpg")
        img = img.resize((350, 400))
        self.petcare.img = ImageTk.PhotoImage(img)
        self.petcare['image'] = self.petcare.img
        self.petcare.place(x = 1110, y = 200)

        def open_web_browser(event):
            webbrowser.open_new("https://shorturl.at/dhopI")  # Replace "https://example.com" with your desired URL

        # Bind the function to the image label
        self.petcare.bind('<Button-1>', open_web_browser)

    def sellerclass(self):

        self.login2.destroy()
        
        self.login9 = Frame(self.root, width = 2000, height = 2000, bg = '#e6e6fa')
        self.login9.place(x = 265, y = 0)

        self.label = Label(self.login9, text="Select an image:")
        self.label.place(x = 20, y = 150)

        self.select_button = Button(self.login9, text="Select Image", command=self.select_image)
        self.select_button.place(x = 100, y = 150)

        self.description_pet = Label(self.login9, text="Pet type")
        self.description_pet.place(x = 20, y = 175)

        self.description_pet_entry = Entry(self.login9)
        self.description_pet_entry.place(x = 100, y = 175)

        self.description_label = Label(self.login9, text="Breed")
        self.description_label.place(x = 20, y = 250)

        self.description_breed_entry = Entry(self.login9)
        self.description_breed_entry.place(x = 100, y = 250)

        self.description_age = Label(self.login9, text="Age")
        self.description_age.place(x = 20, y = 325)

        self.description_age_entry = Entry(self.login9)
        self.description_age_entry.place(x = 100, y = 325)

        self.description_gender = Label(self.login9, text="Gender")
        self.description_gender.place(x = 20, y = 400)

        self.description_gender_entry = Entry(self.login9)
        self.description_gender_entry.place(x = 100, y = 400)

        self.description_size = Label(self.login9, text="Size")
        self.description_size.place(x = 20, y = 475)

        self.description_size_entry = Entry(self.login9)
        self.description_size_entry.place(x = 100, y = 475)

        self.description_descr = Label(self.login9, text="Description")
        self.description_descr.place(x = 20, y = 550)

        self.description_entry = Entry(self.login9)
        self.description_entry.place(x = 100, y = 550)

        self.save_button = Button(self.login9, text="Save Image", command=self.save_image)
        self.save_button.place(x = 300, y = 650)

    def insert_image_into_database(self, image_data):
        try:
            # SQL query to insert image data into database
            sql = "INSERT INTO images (image_data) VALUES (%s)"
            self.cursor.execute(sql, (image_data,))
            self.db.commit()
            print("Image saved to database successfully")
        except Exception as e:
            print("Error occurred while saving image:", e)
    
    def select_image(self):
        file_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", ".png;.jpg;*.jpeg")])
        if file_path:
            self.display_selected_image(file_path)
    
    def display_images(self):
        self.inner_frame.destroy()  # Destroy previous inner frame
        self.inner_frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor=NW)

        cursor.execute("SELECT file_path, image, pettype FROM images")
        self.images = cursor.fetchall()

        row, col = 0, 0
        for image_name, image_data, petttype, breedd, agee, genderr, sizee, pricee, petdescc in self.images:
            with open(image_name, 'wb') as img_file:
                img_file.write(image_data)

            image = Image.open(image_name)
            image = image.resize((200, 200))
            photo = ImageTk.PhotoImage(image)

            label = Label(self.inner_frame, image=photo, text=petttype, compound=tk.TOP)
            label.image = photo
            label.grid(row=row, column=col, padx=10, pady=10)

            col += 1
            if col == 3: 
                row += 1
                col = 0

        self.inner_frame.update_idletasks()  
        self.canvas.config(scrollregion=self.canvas.bbox("all")) 
    
    def display_selected_image(self, file_path):
        image = Image.open(file_path)
        image = image.resize((200, 200)) 
        photo = ImageTk.PhotoImage(image)

        self.label.config(image=photo)
        self.label.image = photo
        self.selected_image_path = file_path


    def save_image(self):
        image_data = None 
        if hasattr(self, 'selected_image_path'):
            with open(self.selected_image_path, 'rb') as image_file:
                image_data = image_file.read()

            image_name = self.selected_image_path.split('/')[-1]  # Extract the image name
            # self.insert_image_into_database(image_data)
            getbreed = self.description_breed_entry.get()
            getage = self.description_age_entry.get()
            getgender = self.description_gender_entry.get()
            getsize = self.description_size_entry.get()
            getpettype = self.description_pet_entry.get()

        try:
            # Check if image_data is not None before executing the database operations
            if image_data is not None:
                # Using parameterized query to insert image data
                query = "INSERT INTO images (image, breed, age, gender, size, petname) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (image_data, getbreed, getage, getgender, getsize, getpettype))
                conn.commit()
                print("Image saved to the database.")
        
        except mysql.connector.Error as e:
            print(f"Error: {e}") 


    def visit_again(self):
        
        self.login1.destroy()
        self.login2.destroy()

        self.label2 = tk.Label(self.root)
        img = Image.open(r"C:/Users/priya/Desktop/pythonproject/source/visitagain.jpg")
        img = img.resize((1550, 1200))
        self.label2.img = ImageTk.PhotoImage(img)
        self.label2['image'] = self.label2.img
        self.label2.pack(fill=tk.BOTH, expand=True)  

    def funhomepage(self):
        self.login11 = Frame(self.root, width = 2000, height = 2000, bg = '#9c9cb5')
        self.login11.place(x = 265, y = 0)

        self.homepage = tk.Label(self.root)
        img = Image.open(r"C:/Users/priya/Desktop/pythonproject/source/homepageimg.jpg")
        img = img.resize((1275, 800))
        self.homepage.img = ImageTk.PhotoImage(img)
        self.homepage['image'] = self.homepage.img
        self.homepage.place(x = 265, y = 0)

        root.title("Adopt pets don't shop")
    def buyerclass(self):
        self.login2.destroy()

        self.login13 = Frame(self.root, width = 2000, height = 2000, bg = '#e6e6fa')
        self.login13.place(x = 265, y = 0)

        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=True)

        self.scrollbar = Scrollbar(self.frame, orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill="y", expand=True, padx = 0, pady = 0)

        self.canvas = Canvas(self.frame, yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.scrollbar.config(command=self.canvas.yview)

        self.inner_frame = Frame(self.canvas) 
        self.canvas.create_window((265, 0), window=self.inner_frame, anchor=NW)

        self.inner_frame.bind("<Configure>", self.on_frame_configure)

        self.display_images()

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def careclass(self):
        self.login2.destroy()

        self.petscare = Frame(self.root, width = 2000, height = 2000, bg = '#e6e6fa')
        self.petscare.place(x = 265, y = 0)
        self.dogimage = PhotoImage(file='findog.png')
        self.dogimage_button = Button(root, image=self.dogimage, command=self.careclassactiondog, border=0, bg='#e6e6fa', width=200, height=200)
        self.dogimage_button.place(x = 350, y=300)

        self.catimage = PhotoImage(file='fcat.png')
        self.catimage_button = Button(root, image=self.catimage, command=self.careclassactioncat, border=0, bg='#e6e6fa', width=200, height=200)
        self.catimage_button.place(x = 650, y=300)

        self.birdimage = PhotoImage(file='fbird.png')
        self.birdimage_button = Button(root, image=self.birdimage, command=self.careclassactionbird, border=0, bg='#e6e6fa', width=200, height=200)
        self.birdimage_button.place(x = 950, y=300)

        self.rabbitimage = PhotoImage(file='frabbit.png')
        self.rabbitimage_button = Button(root, image=self.rabbitimage, command=self.careclassactionrabbit, border=0, bg='#e6e6fa', width=200, height=200)
        self.rabbitimage_button.place(x = 1250, y=270)

    def careclassactiondog(self):
        self.dogimage_button.destroy()
        self.dogimage = None
        self.catimage_button.destroy()
        self.cateimage = None
        self.catimage_button.destroy()
        self.catimage = None
        self.birdimage_button.destroy()
        self.birdimage = None
  
        self.aboutdogcare = tk.Label(self.root)
        img = Image.open(r"C:/Users/priya/Desktop/pythonproject/source/doggcare.jpg")
        img = img.resize((1275, 800))
        self.aboutdogcare.img = ImageTk.PhotoImage(img)
        self.aboutdogcare['image'] = self.aboutdogcare.img
        self.aboutdogcare.place(x = 265, y = 0)

    def careclassactioncat(self):
        self.petscare.destroy()
        self.aboutcatcare = tk.Label(self.root)
        img = Image.open(r"C:/Users/priya/Desktop/pythonproject/source/catcare.jpg")
        img = img.resize((1275, 800))
        self.aboutcatcare.img = ImageTk.PhotoImage(img)
        self.aboutcatcare['image'] = self.aboutcatcare.img
        self.aboutcatcare.place(x = 265, y = 0)

    def careclassactionbird(self):
        self.petscare.destroy()
        self.aboutbirdcare = tk.Label(self.root)
        img = Image.open(r"C:/Users/priya/Desktop/pythonproject/source/birdcare.jpg")
        img = img.resize((1275, 800))
        self.aboutbirdcare.img = ImageTk.PhotoImage(img)
        self.aboutbirdcare['image'] = self.aboutbirdcare.img
        self.aboutbirdcare.place(x = 265, y = 0)

    def careclassactionrabbit(self):
        self.petscare.destroy()
        self.aboutrabbitcare = tk.Label(self.root)
        img = Image.open(r"C:/Users/priya/Desktop/pythonproject/source/rabbitcare.jpg")
        img = img.resize((1275, 800))
        self.aboutrabbitcare.img = ImageTk.PhotoImage(img)
        self.aboutrabbitcare['image'] = self.aboutrabbitcare.img
        self.aboutrabbitcare.place(x = 265, y = 0)


root = Tk()
root.title('LOVELY HABITAT')
root.geometry('550x350+550+200')
root.resizable(True, True)
login = Login(root)
root.mainloop()