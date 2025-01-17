from tkinter import Tk, Label
from PIL import ImageTk
from PIL.Image import Image

# from PIL import Image, ImageTk

root = Tk()
bg = Image.open('..//assets//bg.png')
#bg = bg.resize((width, height))

bg = ImageTk.PhotoImage(bg)
lbl = Label(root, image= bg)
lbl.pack()
root.mainloop()


from tkinter import Tk, Label, Frame
from PIL import Image, ImageTk

class YourClass:
    def __init__(self):
        self.root = Tk()
        self.bg = Image.open('..//assets//bg.png')
        # self.bg = self.bg.resize((width, height))

        self.bg = ImageTk.PhotoImage(self.bg)
        self.lbl = Label(self.root, image=self.bg)
        self.lbl.pack()

        self.d_frame_text = Frame(self.root, width=10, height=200, bg='black')
        self.d_frame_text.place(x=5, y=5)

        self.d_name = Label(self.d_frame_text, text='kjgehku h24oy jhauhu hi adjhcufow asgdiegwif jrglvijiltrj rgkjlerijg kadjfilwjei', font=fonts, bg='pink', fg='white', width=10)
        self.d_name.place(x=5, y=25)

    def run(self):
        self.root.mainloop()

# Create an instance of YourClass
your_instance = YourClass()
# Run the main loop
your_instance.run()



# self.d_frame_text = Frame(self.root, width = 10, height = 200, bg = 'black')
# self.d_frame_text.place(x = 5, y = 5)
# self.d_name = Label(self.d_frame_text, text = 'kjgehku h24oy jhauhu hi adjhcufow asgdiegwif jrglvijiltrj rgkjlerijg kadjfilwjei', font = fonts, bg = 'pink', fg = 'white', width = 10)
# self.d_name.place(x = 5, y = 25)