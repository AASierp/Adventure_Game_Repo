import tkinter as Tk
from Dialogue import intro


class MyGUI:

    def __init__(self):

        self.root = Tk.Tk()

        self.root.geometry("1500x800")

        self.label = Tk.Label(self.root, text="test", font=("Arial", 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = Tk.Text(self.root, height=1, font=("Arial", 18))
        self.textbox.pack(padx=10, pady=10)

        self.button = Tk.Button(self.root, text="Submit", font=(
            'Papyrus', 14), command=self.submit)
        self.button.pack(padx=0, pady=10)

        self.root.mainloop()

    def submit(self):

        self.root = Tk.Tk()

        self.root.geometry("1500x800")

        self.label = Tk.Label(self.root, text=intro, font=("Arial", 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = Tk.Text(self.root, height=1, font=("Arial", 18))
        self.textbox.pack(padx=10, pady=10)

        self.button = Tk.Button(self.root, text="Submit", font=(
            'Papyrus', 14), command=self.submit)
        self.button.pack(padx=0, pady=10)

        self.root.mainloop()


MyGUI()
