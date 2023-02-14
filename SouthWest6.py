import tkinter as Tk
from tkinter import PhotoImage
import Dialogue as DI
import tkinter.messagebox
import random
import South7 as S7


class SouthWest6:
    def __init__(self):

        root = Tk.Tk()

        #width = root.winfo_screenwidth()
        #height = root.winfo_screenheight()
        #root.geometry("%dx%d" % (width, height))

        root.geometry("1920x1080")

        root.title("Adventure Game")

        bgimg = random.choice(
            ["images\max.png", "images\mistyclearing.png", "images\max.png"])

        Canvas = Tk.Canvas(root, bg="blue", height=250, width=400)
        filename = PhotoImage(file=bgimg)
        background_label = Tk.Label(root, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        Canvas.pack()

        if bgimg == "images\max.png":
            label = Tk.Label(root, text=DI.SouthWest6_text1,
                             borderwidth=30, font=("Papyrus 20 bold"))
            label.config(bg="linen")
            label.pack(padx=0, pady=0)
        else:
            label = Tk.Label(root, text=DI.SouthWest6_text0,
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
                    "ERROR", """You stumble stupidly into the river and drowned..."GAME OVER"...Just kidding! pick another direction stupid.""")
            elif direction.lower() == ("east"):
                root.destroy()
                S7.South7()
            elif direction.lower() == ("west"):
                tkinter.messagebox.showinfo(
                    "ERROR", """You fall over 100 feet to your demise. Try again...""")
            elif direction.lower() == ("south"):
                tkinter.messagebox.showinfo(
                    "ERROR", "You smack your head against the cliff face. Maybe that will knock some sense into you.")
            elif direction.lower() == ("help"):
                label = Tk.Label(root, text=DI.SouthWest6_text0,
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
