from tkinter import Tk, BOTH, RAISED, RIGHT, LEFT, BooleanVar
from tkinter.ttk import Frame, Button, Style, Checkbutton


class Exemple(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.style = Style()
        self.style.theme_use("default")

        self.master.title("convertisseur")
        self.pack(fill = BOTH, expand = 1)

        frame = Frame(self, relief = RAISED, borderwidth = 1)
        frame.pack(fill = BOTH, expand = True)


        bouton = Button(self, text = "Quit",
                        command = self.quit)
        bouton.pack(side = RIGHT, padx = 5, pady = 5)
        bouton1 = Button(self, text = "stay")
        bouton1.pack(side = RIGHT, padx = 5, pady = 5)

        self.var = BooleanVar()
        cb = Checkbutton(self, text = "Montre le titre",
                         variable = self.var, command = self.onClick)
        self.var.set(True)
        cb.pack(side = LEFT, padx = 5, pady = 5)

    def onClick(self):
        if self.var.get() == True:
            self.master.title("convertisseur")
        else:
            self.master.title("")

def main():
    racine = Tk()
    racine.geometry("250x150+300+300")
    app = Exemple()
    racine.mainloop()


if __name__ == "__main__":
    main()
