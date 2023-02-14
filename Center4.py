import tkinter as Tk
from tkinter import PhotoImage
import Dialogue as DI
import tkinter.messagebox
import random


class Center4:
    def __init__(self):

        root = Tk.Tk()

        #width = root.winfo_screenwidth()
        #height = root.winfo_screenheight()
        #root.geometry("%dx%d" % (width, height))

        root.geometry("1920x1080")

        root.title("Adventure Game")

        bgimg = random.choice(
            ["images\maninwoods.png", "images\mistyclearing.png", "images\maninwoods.png"])

        Canvas = Tk.Canvas(root, bg="blue", height=200, width=400)
        filename = PhotoImage(file=bgimg)
        background_label = Tk.Label(root, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        Canvas.pack()

        if bgimg == "images\maninwoods.png":
            label = Tk.Label(root, text=DI.west0x1_text1,
                             borderwidth=30, font=("Papyrus 20 bold"))
            label.config(bg="linen")
            label.pack(padx=0, pady=0)
        else:
            label = Tk.Label(root, text=DI.west0x1_text0,
                             borderwidth=30, font=("Papyrus 20 bold"))
            label.config(bg="linen")
            label.pack(padx=0, pady=0)

        entry = Tk.Entry(root, width=100, borderwidth=5,
                         font="Papyrus 14 bold")
        entry.pack(padx=20, pady=20)

        def myClick():
            direction = entry.get()
            if direction.lower() == ("north"):
                pass
            elif direction.lower() == ("east"):
                pass
            elif direction.lower() == ("west"):
                tkinter.messagebox.showinfo(
                    "ERROR", """You stumble stupidly into the river and drowned..."GAME OVER"...Just kidding! pick another direction stupid.""")
            elif direction.lower() == ("south"):
                tkinter.messagebox.showinfo(
                    "ERROR", "You smack your head against the cliff face. Maybe that will knock some sense into you.")
            else:
                tkinter.messagebox.showinfo(
                    "ERROR.", "That is NOT a valid option. Please try again.")

        button = Tk.Button(root, text="Submit", font=(
            'Papyrus 16 bold'), command=myClick)
        button.pack(padx=0, pady=10)

        root.mainloop()
