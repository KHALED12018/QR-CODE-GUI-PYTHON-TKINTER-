import tkinter as tk
import qrcode
import tkinter.colorchooser
from PIL import Image, ImageTk

def create_qr_code(text, color):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color, back_color="white")
    return img

def change_color():
    color = tkinter.colorchooser.askcolor(title="Select QR Code Color")[1]
    image = create_qr_code("example text", color)
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo

def save_image():
    path = entry.get()
    image = create_qr_code("example text", color_var.get())
    image.save(path)
    label_path.config(text="Image saved to: " + path)

root = tk.Tk()
root.geometry("400x400")
root.title("QR_Code yp DRAGON-NOIR2023")

button_color = tk.Button(root, text="Select Color", command=change_color)
button_color.pack()

entry = tk.Entry(root)
entry.pack()

button_save = tk.Button(root, text="Save Image", command=save_image)
button_save.pack()

label_path = tk.Label(root)
label_path.pack()

image = create_qr_code("example text", "black")
photo = ImageTk.PhotoImage(image)
label = tk.Label(image=photo)
label.pack()

root.mainloop()
