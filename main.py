# importing libraries
from PIL import Image, ImageTk, ImageDraw, ImageFont
import random
import emoji_set
from tkinter import Tk, Label, Button, filedialog
import ctypes



# increasing dpi
ctypes.windll.shcore.SetProcessDpiAwareness(2)
# create window
root = Tk()
root.geometry('900x500')
root.title('emojitar')

# add background image
img = ImageTk.PhotoImage(Image.open('bk_img.png'))
panel = Label(root, image=img)
panel.pack()


def run():
    color = random.choice(emoji_set.colour_combs())
    emoji = random.choice(emoji_set.pick_emoji())[0]
    img = Image.new('RGB', (3000, 3000), color[0])
    img_draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('NotoEmoji-Regular.ttf', 2000)
    img_draw.text((1500, 1500), emoji, fill=color[1], font=font, anchor='mm')
    img.show()
    img.save(filedialog.asksaveasfilename(defaultextension='png'))  


# create generate button
button = Button()
button_image = ImageTk.PhotoImage(Image.open('generate.png'))
button = Button(image=button_image, borderwidth=0, command=lambda: run())
button.place(x=348.4, y=287.9, width=180, height=60)
root.mainloop()