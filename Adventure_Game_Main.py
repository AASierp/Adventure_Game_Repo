
import tkinter as Tk
import Classes as CL

root = Tk.Tk()

root.geometry("1500x1300")

root.configure(bg="tan")

root.title("Title")

label = Tk.Label(root, text="""   STORY """, font=("Papyrus 18 bold"))

label.pack(padx=0, pady=40)
textbox = Tk.Text(root, height=1, font=('Papyrus 14 bold'))
textbox.pack(padx=0, pady=0)

button = Tk.Button(root, text="Submit", font="Papyrus 12 bold")
button.pack(padx=0, pady=10)
root.mainloop()
