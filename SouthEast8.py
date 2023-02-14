import tkinter as Tk
from tkinter import PhotoImage
import Dialogue as DI
import tkinter.messagebox
import random
import South7 as S7


class SouthEast8:
    def __init__(self):

        axe = 1

        root = Tk.Tk()

        # width = root.winfo_screenwidth()
        # height = root.winfo_screenheight()
        # root.geometry("%dx%d" % (width, height))

        root.geometry("1920x1080")

        root.title("Adventure Game")

        Canvas = Tk.Canvas(root, bg="blue", height=200, width=400)
        filename = PhotoImage(file="images\SouthEast8.png")
        background_label = Tk.Label(root, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        Canvas.pack()

        if axe == 1:
            label = Tk.Label(root, text=DI.SouthEast8_text1,
                             borderwidth=30, font=("Papyrus 20 bold"))
            label.config(bg="linen")
            label.pack(padx=0, pady=0)

        else:
            label = Tk.Label(root, text=DI.SouthEast8_text0,
                             borderwidth=30, font=("Papyrus 20 bold"))
            label.config(bg="linen")
            label.pack(padx=0, pady=0)

        entry = Tk.Entry(root, width=100, borderwidth=5,
                         font="Papyrus 14 bold")
        entry.pack(padx=20, pady=20)

        def myClick():
            direction = entry.get()
            if direction.lower() == ("north"):
                tkinter.messagebox.showinfo(
                    "ERROR", """You are blocked by the river, if only there was some way across...""")
            elif direction.lower() == ("east"):
                tkinter.messagebox.showinfo(
                    "ERROR", """You are blocked by dense jungle, keep an eye out for cannibals...""")
            elif direction.lower() == ("west"):
                root.destroy
                S7.South7()
            elif direction.lower() == ("south"):
                tkinter.messagebox.showinfo(
                    "ERROR", "You smack your head against the cliff face. Maybe that will knock some sense into you.")
            elif direction.lower() == ("cut"):
                label = Tk.Label(root, text=DI.SouthEast8_text2,
                                 borderwidth=30, font=("Papyrus 20 bold"))
                label.config(bg="linen")
                label.pack(padx=0, pady=0)
            else:
                tkinter.messagebox.showinfo(
                    "ERROR.", "That is NOT a valid option. Please try again.")

        button = Tk.Button(root, text="Submit", font=(
            'Papyrus 16 bold'), command=myClick)
        button.pack(padx=0, pady=10)

        root.mainloop()
