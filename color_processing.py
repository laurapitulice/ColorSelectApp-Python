import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel
from PIL import Image, ImageTk
import cv2
import numpy as np
from sklearn.cluster import KMeans

class ColorSelectApp:
    def __init__(self, root):

        # main window setup
        self.root = root
        self.root.title("ColorSelect App")
        self.root.geometry("1600x900")

        # image data init
        self.path = None
        self.image = None
        self.displayImg = None

        # setting up the toolbar
        self.toolbar = tk.Frame(root, width=300, height=500,)
        self.toolbar.pack(side="top", padx=10, pady=20)

        self.button1 = tk.Button(self.toolbar, text="Load Your Image",  width=25, command=self.load_image)
        self.button1.pack(side="left", padx = 10)

        self.button2 = tk.Button(self.toolbar, text="Generate Color Palette", width=25, command=self.run_kmeans, state="disabled")
        self.button2.pack(side="left", padx = 10)
        
        self.button3 = tk.Button(self.toolbar, text="Exit", width=10, command=root.destroy)
        self.button3.pack(side="right", padx = 10)

        # text information
        self.text = tk.Label(root, text="Press \"Load your image\" to begin!", font=("Georgia", 14))
        self.text.pack()

        # defining canvas for image
        self.canvas = tk.Canvas(root, bg="lightgray", cursor="heart")
        self.canvas.pack(padx=20, pady=10)
        self.canvas.bind("<Button-1>", self.get_pixel_color)

        # setting up frame for k-means palette
        self.palette_frame = tk.Frame(root)
        self.palette_frame.pack(side="bottom", pady=40) 

    def load_image(self):
        # extracting the image path
        self.path = filedialog.askopenfilename(filetypes=[("Images", "*.jpg *.png *.jpeg")])
        if not self.path:
            return

        # loading the image using PIL in RGB format
        self.image = Image.open(self.path).convert("RGB")
        
        # resizing the image to fit in the canvas
        self.image.thumbnail((800, 600))
        
        self.displayImg = ImageTk.PhotoImage(self.image)
        
        # showing the image
        self.canvas.config(width=self.image.width, height=self.image.height)
        self.canvas.create_image(0, 0, anchor="nw", image=self.displayImg)
        
        self.button2.config(state="normal")
        self.text.config(text="Click on the image.")

    def copy_to_clipboard(self, text_to_copy):
        self.root.clipboard_clear()  
        self.root.clipboard_append(text_to_copy)
        
    def get_pixel_color(self, event):
        if not self.image:
            return

        # extracting the colors from coordinates selected by mouse click
        if event.x < self.image.width and event.y < self.image.height:
            r, g, b = self.image.getpixel((event.x, event.y))
            hex_color = f"#{r:02x}{g:02x}{b:02x}"
            
            self.text.config(text=f"HEX: {hex_color}")
            self.text.bind("<Button-1>", lambda e: self.copy_to_clipboard(hex_color))
            
            # pop-up windows with the selected colors
            self.color_window = Toplevel(root)
            self.color_window.geometry("220x220")
            self.color_window.configure(bg=hex_color)
            self.color_window.title(f"{hex_color}")

    def run_kmeans(self):
        # converting the image from PIL to NumPy/OpenCV
        img_np = np.array(self.image)

        pixels = img_np.reshape((-1, 3))
        
        # applying K-Means for 5 dominant colors
        kmeans = KMeans(n_clusters=5, n_init=10)
        kmeans.fit(pixels)
        dominant_colors = kmeans.cluster_centers_.astype(int)

        # clearing the old palette
        for widget in self.palette_frame.winfo_children():
            widget.destroy()

        # showing the new colors
        for color in dominant_colors:
            hex_c = f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"
            swatch = tk.Frame(self.palette_frame, bg=hex_c, width=60, height=60)
            swatch.pack(side="left", padx=5)
root = tk.Tk()
app = ColorSelectApp(root)
root.mainloop()