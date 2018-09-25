from tkinter import Frame, Button, Tk, Entry


class Dcomponent:

    def __init__(self, master=None):
        frame = Frame(master)
        frame.grid()
        self.entryButton = Entry(frame)
        self.entryButton.grid(padx=96, pady=240)

        self.printButton = Button(frame, text="press me pls", command=self.printmessage)
        self.printButton.grid(padx=1, pady=0)

        self.terminate = Button(frame, text="Kill me pls", command=frame.quit)
        self.terminate.grid(padx=1, pady=0)

    def printmessage(self):
        print("Thx f0r pressing")


root = Tk()
Window = Dcomponent(root)
root.geometry("480x320")
root.mainloop()
