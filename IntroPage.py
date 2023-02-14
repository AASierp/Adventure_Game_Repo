import tkinter as Tk
from tkinter import PhotoImage
import Dialogue as DI
import tkinter.messagebox
import SouthWest6 as SW6
import SouthEast8 as SE8
import Center4 as C4


class IntroPage:

    def __init__(self):

        root = Tk.Tk()

        #width = root.winfo_screenwidth()
        #height = root.winfo_screenheight()
        #root.geometry("%dx%d" % (width, height))
        root.geometry("1920x1080")

        root.title("A Hero's Journey")

        Canvas = Tk.Canvas(root, bg="blue", height=250, width=400)
        filename = PhotoImage(file="images\imgintro.png")
        background_label = Tk.Label(root, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        Canvas.pack()

        label = Tk.Label(root, text=DI.intro, borderwidth=30,
                         font=("Papyrus 22 bold"))
        label.config(bg="linen")
        label.pack(padx=0, pady=40)

        entry = Tk.Entry(root, width=50, borderwidth=5, font="Papyrus 16 bold")
        entry.pack(padx=20, pady=20)

        def myClick():
            direction = entry.get()
            if direction.lower() == ("north"):
                tkinter.messagebox.showinfo(
                    "ERROR", """You stumble stupidly into the river and drowned..."GAME OVER"...Just kidding! pick another direction stupid.""")
            elif direction.lower() == ("east"):
                root.destroy()
                SE8.SouthEast8()
            elif direction.lower() == ("west"):
                root.destroy()
                SW6.SouthWest6()
            elif direction.lower() == ("south"):
                tkinter.messagebox.showinfo(
                    "ERROR", "Someone needs to work on their reading comprehension.")
            else:
                tkinter.messagebox.showinfo(
                    "ERROR.", "That is NOT a valid option. Please try again.")

        button = Tk.Button(root, text="Submit", font=(
            'Papyrus 16 bold'), command=myClick)
        button.pack(padx=0, pady=10)

        root.mainloop()


IntroPage()
