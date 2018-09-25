from tkinter import Frame, Button, Tk, Entry


class BoardFrame(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_components()

    def init_components(self):
        self.master.title("School of life")
        self.columnconfigure(min("500"))
        addPlayer1 = Button(root, text="Add player").place(x=0, y=0)
        addPlayer2 = Button(root, text="Add player").place(x=0, y=36)
        addPlayer3 = Button(root, text="Add player").place(x=0, y=72)
        addPlayer4 = Button(root, text="Add player").place(x=0, y=108)
        addPlayer5 = Button(root, text="Add player").place(x=0, y=141)

        # The entries correspond with the player numbers. So entry 1 is designated for player 1 and visa versa.
        Entry1 = Entry(root).place(x=100, y=0)
        Entry2 = Entry(root).place(x=100, y=35)
        Entry3 = Entry(root).place(x=100, y=71)
        Entry4 = Entry(root).place(x=100, y=106)
        Entry5 = Entry(root).place(x=100, y=141)

        # addplayer1 = Button(root, text="Add player").grid(row=9, column=1, padx=5)
        # addplayer2 = Button(root, text="Add player").grid(row=1, column=2, padx=8)
        # addplayer3 = Button(root, text="Add player").grid(row=1, column=3, padx=8)
        # addplayer4 = Button(root, text="Add player").grid(row=1, column=4, padx=8)
        # addplayer5 = Button(root, text="Add player").grid(row=1, column=5, padx=8, pady=10)


root = Tk()
root.geometry("412x200")
window = BoardFrame(root)
root.mainloop()
