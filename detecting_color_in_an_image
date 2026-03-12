from tkinter import Tk, Canvas, Toplevel, Label
from PIL import Image, ImageTk

def show_color(event):
    x, y = event.x, event.y
# Obține culoarea pixelului din imagine
    r, g, b = image.getpixel((x, y))
    hex_color = f'#{r:02x}{g:02x}{b:02x}'

# Creează o fereastră pop-up
    color_window = Toplevel(root)
    color_window.geometry("200x200")
    color_window.configure(bg=hex_color)
    color_window.title("Culoare selectată")

# Adaugă textul cu hex-ul sub culoare
    label = Label(color_window, text=f"Hex: {hex_color}", bg=hex_color, fg="white", font=("Arial", 14))
    label.pack(expand=True)

# Fereastra principală
root = Tk()
root.title("Alege o culoare")

# Încarcă imaginea și convertește-o în RGB
image_path = "crin.jpg"
image = Image.open(image_path).convert("RGB")
tk_image = ImageTk.PhotoImage(image)

# Afișează imaginea pe un Canvas
canvas = Canvas(root, width=image.width, height=image.height)
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=tk_image)

# Eveniment pentru click pe imagine
canvas.bind("<Button-1>", show_color)

# Pornește aplicația
root.mainloop()