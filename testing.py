import tkinter as Tk
from tkinter import PhotoImage
import Dialogue as DI
import tkinter.messagebox
import SouthWest6 as SW6
from tkinter import font



class intro_page:
    def __init__(self):

        root = Tk.Tk()

        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.geometry("%dx%d" % (width, height))

        root.title("Adventure Game")

        Canvas = Tk.Canvas(root, bg="blue", height=350, width=400)
        filename = PhotoImage(file="imgintro.png")
        background_label = Tk.Label(root, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        Canvas.pack()

        label = Tk.Label(root, text=DI.intro, borderwidth=30,
                         font=("Constantia 22"))
        label.config(bg="paleGoldenrod")
        label.pack(padx=0, pady=40)

        entry = Tk.Entry(root, width=100, borderwidth=5)
        entry.pack(padx=20, pady=20)

        def myClick(self):
            direction = entry.get()
            if direction.lower() == ("north"):
                pass
            elif direction.lower() == ("east"):
                pass
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
            'Papyrus', 14), command=myClick)
        button.pack(padx=0, pady=10)

        root.mainloop()


intro_page()
