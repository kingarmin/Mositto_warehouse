from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\10.armin\Desktop\Mositto_anbar\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("850x780")
window.configure(bg = "#FFFFFF")

frame_start=Frame(window)
canvas1 = Canvas(
    frame_start,
    bg = "#FFFFFF",
    height = 780,
    width = 850,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

image_image_1 = PhotoImage(master=frame_start,
    file=relative_to_assets("image_1.png"))
image_1 = canvas1.create_image(
    425.00000000000045,
    20.0,
    image=image_image_1
)

canvas1.create_text(
    354.00000000000045,
    4.0,
    anchor="nw",
    text="Start menu",
    fill="#000000",
    font=("Inter ExtraBold", 24 * -1)
)

button_image_1 = PhotoImage(master=frame_start,
    file=relative_to_assets("button_1.png"))
button_1 = Button(frame_start,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
canvas1.create_window(250, 257, window=button_1, width=130, height=134)

button_image_2 = PhotoImage(master=frame_start,
    file=relative_to_assets("button_2.png"))
button_2 = Button(frame_start,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
canvas1.create_window(582, 256, window=button_2, width=130, height=135)

canvas1.create_text(
    532.0000000000005,
    395.0,
    anchor="nw",
    text="Add items",
    fill="#000000",
    font=("Inter ExtraBold", 24 * -1)
)

canvas1.create_text(
    189.00000000000045,
    395.0,
    anchor="nw",
    text="search items",
    fill="#000000",
    font=("Inter ExtraBold", 24 * -1)
)

canvas1.pack()
frame_start.pack()

window.resizable(False, False)
window.mainloop()