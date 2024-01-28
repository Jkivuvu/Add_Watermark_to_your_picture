from tkinter import Label, filedialog
from PIL import ImageTk, Image


def Upload():
    global my_image, watermark, a
    watermark = Image.open('Logo.png')
    filename = filedialog.askopenfilename(initialdir='/', title='Select a picture',
                                          filetypes=(('png files', '*.png'), ('all files', '*.*')))
    a = Image.open(filename)
    a.paste(watermark, (0, 0), mask=watermark)

    my_image = ImageTk.PhotoImage(a)
    my_image_label = Label(image=my_image)
    my_image_label.grid(row=1, column=0, columnspan=6, pady=25, padx=25)


def Save():
    filename = filedialog.asksaveasfile(mode='wb', defaultextension='.png')
    if not filename:
        return
    a.save(filename)
