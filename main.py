import tkinter as tk
from tkinter import Button

from Functions import Upload, Save

window = tk.Tk()
window.title('Watermark GUI')
button_upload = Button(window, text='Upload', command=Upload)
button_upload.grid(row=0, column=0, columnspan=2)

button_save = Button(window, text='Save', command=Save)
button_save.grid(row=0, column=2, columnspan=2)

button_quit = Button(window, text='Exit', command=window.quit)
button_quit.grid(row=0, column=4, columnspan=2)
window.mainloop()
