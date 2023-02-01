
import tkinter as Tk

root = Tk.Tk()

root.geometry("1500x1300")

root.configure(bg="tan")

root.title("The Adventure of Perry Trotter and the Heavily Restricted Forest")

label = Tk.Label(root, text="""    Welcome \n
to The Adventure of Perry Trotter and the Heavily Restricted Forest!
Today, you will embark on the adventure of a life time as you and Perry navigate 
the treacherous path through the heavily restricted forest in search of fame and 
fortune!

    First a little background side story flashback vignette is in order...
Young Perry grew up to be a poor orphan. He was able to find meager employment as 
an errand man for his local grocer, who also happened to be his cruel and unusual uncle.
His uncle frequently beat and berated young Perry. It wasn't long before the young middle aged Perry
became fed up and dissatisfied with his lot in life. But the fates had not yet fully abandoned young Perry. 
One brisk spring morning a long awaited letter arrived with Perry's name on it.
It was his acceptance letter to janitorial school! At long last Perry would be pursuing his
porcelain dreams! Though Perry's uncle was not pleased, he did not attempt to prevent Perry's 
departure as he regarded our young hero as more of a burden than an asset...
    
    So, with is ruck sack upon his back and an old broomstick in hand, he began his long journey.
Now, normally, one would simply take a cabby around the forest. However, since he was on foot, it was 
much quicker to simply go through the forest.......""", font=("Papyrus 18 bold"))

label.pack(padx=0, pady=40)
textbox = Tk.Text(root, height=1, font=('Papyrus 14 bold'))
textbox.pack(padx=0, pady=0)

button = Tk.Button(root, text="Submit", font="Papyrus 12 bold")
button.pack(padx=0, pady=10)
root.mainloop()
