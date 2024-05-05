import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw

class RoundedWindow(tk.Toplevel):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.overrideredirect(True)  # Remove window decorations
        self.create_rounded_window()

    def create_rounded_window(self):
        width, height = 683, 384
        self.geometry(f"{width}x{height}+{self.winfo_screenwidth() // 2 - width // 2}+{self.winfo_screenheight() // 2 - height // 2}")
        self.canvas = tk.Canvas(self, width=width, height=height, highlightthickness=0)
        self.canvas.pack()
        # Draw rounded rectangle mask
        mask = Image.new("L", (width, height), 0)
        draw = ImageDraw.Draw(mask)
        draw.rectangle([(0, 0), (width, height)], fill=255)
        draw.rectangle([(10, 10), (width - 10, height - 10)], fill=0)
        draw.rectangle([(20, 20), (width - 20, height - 20)], fill=255)
        self.mask = mask

    def show(self):
        self.wm_attributes("-transparentcolor", "white")
        self.attributes("-alpha", 0.9)  # Set transparency level
        self.update_idletasks()
        self.mask_image = ImageTk.PhotoImage(image=self.mask)
        self.canvas.create_image(0, 0, anchor="nw", image=self.mask_image)

        # Your UI elements here
        tk.Label(self, text="Welcome to [Hotel System]", font=("Arial", 20, "bold")).place(x=180, y=50)
        tk.Label(self, text="Would you like to INSERT or UPDATE data?", font=("Arial", 20, "bold")).place(x=70, y=160)

        insert_button = tk.Button(self, text="Insert", command=self.insert_data, bg="#DEAC80", fg="#000000")
        insert_button.place(x=100, y=250)
        insert_button.config(width=10, height=4)

        update_button = tk.Button(self, text="Update", command=self.update_data, bg="#DEAC80", fg="#000000")
        update_button.place(x=500, y=250)
        update_button.config(width=10, height=4)

        self.mainloop()

    def insert_data(self):
        insert_window = tk.Toplevel(self)
        insert_window.title("Insert Data")
        insert_window.config(background='#F7DCB9')
        # Your insert window code here

    def update_data(self):
        update_window = tk.Toplevel(self)
        update_window.title("Update Data")
        update_window.config(background='#F7DCB9')
        # Your update window code here

root = tk.Tk()
app = RoundedWindow(root)
app.show()
