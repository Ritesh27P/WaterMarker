from tkinter import *
from PIL import ImageTk, Image, ImageDraw, ImageFont
import os


win = Tk()
win.title('Watermarker')
win.geometry("700x500")


def getimg():
    frame = Frame(win, width=600, height=400)
    frame.grid(row=5, column=3)
    frame.place(anchor='center', relx=0.5, rely=0.5)
    image = Image.open(path.get())
    watermark_image = image.copy()
    draw = ImageDraw.Draw(watermark_image)
    font = ImageFont.truetype("arial.ttf", 50)
    draw.text((0, 0), watermark_entry.get(), (0, 0, 0), font=font)
    watermark = ImageTk.PhotoImage(watermark_image.resize((700, 500)))
    watermark_image.show()
    watermark_image.save(os.path.join(save_path.get() + name.get() + '.jpg'))
    label = Label(frame, image=watermark)
    label.grid(row=4, column=1)


# Create a Label Widget to display the text or Image
path_label = Label(win, text='Paste your image here')
path_label.grid(row=1, column=0)
path = Entry(win)
path.grid(row=1, column=2)

watermark_label = Label(win, text='Add your watermark')
watermark_label.grid(row=2, column=0)
watermark_entry = Entry(win)
watermark_entry.grid(row=2, column=2)

save_path_label = Label(win, text='Where to save?')
save_path_label.grid(row=3, column=0)
save_path = Entry(win)
save_path.grid(row=3, column=2)
name_l = Label(win, text='+ Name:')
name_l.grid(row=3, column=3)
name = Entry(win)
name.grid(row=3, column=4)
button = Button(win, text='Download', command=getimg)
button.grid(row=3, column=5)

win.mainloop()
