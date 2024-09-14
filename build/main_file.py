from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
from pathlib import Path
page=None
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("850x780")
window.configure(bg = "#FFFFFF")
window.title("Warehousing system")
frame_start=Frame(window)
def get_entry1_val():
    entry1_val=entry_1.get()
    print(entry1_val)
def switch_to_start():
    canvas1.pack()
    frame_start.pack()
    frame_search.pack_forget()
    canvas2.pack_forget()
    frame_add.pack_forget()
    canvas3.pack_forget()
def switch_to_search():
    canvas1.pack_forget()
    frame_start.pack_forget()
    canvas3.pack_forget()
    frame_add.pack_forget()
    frame_search.pack()
    canvas2.pack()
    print("ok")
def switch_to_add():
    canvas1.pack_forget()
    frame_start.pack_forget()
    frame_search.pack_forget()
    canvas2.pack_forget()
    canvas3.pack()
    frame_add.pack()
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
    command=switch_to_search,
    relief="flat"
)
canvas1.create_window(250, 257, window=button_1, width=130, height=134)

button_image_2 = PhotoImage(master=frame_start,
    file=relative_to_assets("button_2.png"))
button_2 = Button(frame_start,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=switch_to_add,
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

#frame 1 finished
frame_search=Frame(window)
canvas2 = Canvas(
    frame_search,
    bg = "#FFFFFF",
    height = 780,
    width = 850,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
image_image_2 = PhotoImage(master=frame_search,
    file=relative_to_assets("image_1.png"))
image_2 = canvas2.create_image(
    425.0,
    20.0,
    image=image_image_1
)
entry_image_1 = PhotoImage(master=frame_search,
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas2.create_image(
    425.0,
    195.0,
    image=entry_image_1
)
entry_1 = Entry(frame_search,
    bd=0,
    bg="#FFE9E9",
    fg="#000716",
    highlightthickness=0
)
canvas2.create_window(425, 195, window=entry_1, width=750, height=68)
button_image_3 = PhotoImage(master=frame_search,
    file=relative_to_assets("button_3.png"))
button_3 = Button(frame_search,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=get_entry1_val,
    relief="flat",  
    text="Enter", 
    compound="center",
    font=("Inter ExtraBold", 18)
)
canvas2.create_window(425, 274, window=button_3, width=130, height=50)
button_back_image=PhotoImage(master=frame_search,
    file=relative_to_assets("back.png")
)
back_button = Button(frame_search,image=button_back_image,borderwidth=0,highlightthickness=0,command=switch_to_start,relief='flat')
canvas2.create_window(372+125/2,630,window=back_button,width=125,height=125)

canvas2.create_text(
    347.0,
    5.0,
    anchor="nw",
    text="Search menu\n",
    fill="#000000",
    font=("Inter ExtraBold", 24 * -1)
)
# frame_2 finished
frame_add=Frame(window)
canvas3 = Canvas(
    frame_add,
    bg = "#FFFFFF",
    height = 780,
    width = 850,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
image_image_3 = PhotoImage(master=frame_add,
    file=relative_to_assets("image_3.png"))
image_1 = canvas3.create_image(
    425.0,
    20.0,
    image=image_image_3
)
entry_image_2 = PhotoImage(master=frame_add,
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas3.create_image(
    425.0,
    195.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFE9E9",
    fg="#000716",
    highlightthickness=0
)
canvas3.create_window(425,195,window=entry_2,width=750,height=68)
button_image_4 = PhotoImage(master=frame_add,
    file=relative_to_assets("button_4.png"))
button_4 = Button(frame_add,
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat",
    text="Enter", 
    compound="center",
    font=("Inter ExtraBold", 18)
)
canvas3.create_window(425, 274, window=button_4, width=130, height=50)
canvas3.create_text(
    392.0,
    274.0,
    anchor="nw",
    text="Enter\n",
    fill="#000000",
    font=("Inter ExtraBold", 24 * -1)
)
canvas3.create_text(
    324.0,
    5.0,
    anchor="nw",
    text="Add items menu",
    fill="#000000",
    font=("Inter ExtraBold", 24 * -1)
)
button_image_5 = PhotoImage(master=frame_add,
    file=relative_to_assets("button_5.png"))
button_5 = Button(frame_add,
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
canvas3.create_window(125/2,630,window=button_5,width=125,height=125)
button_image_6 = PhotoImage(master=frame_add,
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
canvas3.create_window(850-125/2,630,window=button_6,width=125,height=125)
button_back_image2=PhotoImage(master=frame_add,
    file=relative_to_assets("back.png")
)
back_button2 = Button(frame_add,image=button_back_image2,borderwidth=0,highlightthickness=0,command=switch_to_start,relief='flat')
canvas3.create_window(372+125/2,630,window=back_button2,width=125,height=125)
if page==None:
    page =1
    switch_to_start()
window.resizable(False, False)
window.mainloop()