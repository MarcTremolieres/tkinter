from tkinter.ttk import Frame, Label,Entry
from tkinter import Tk, BOTH, RAISED, RIGHT, LEFT, IntVar, StringVar, END
from conversion import Nombre


class Convertisseur(Frame):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        self.nombre = Nombre(0,10)

        self.master.title("convertisseur")
        self.pack(fill=BOTH, expand=1)
        frame1 = Frame(self, relief = RAISED, borderwidth = 1)
        frame1.pack(fill = BOTH)
        label1 = Label(frame1, text = "Valeur")
        label1.pack(side = LEFT)
        self.valeur = StringVar()
        self.ecriture = StringVar()

        disp_valeur = Entry(frame1, textvar = self.valeur )
        disp_valeur.delete(0, END)
        self.valeur.set(str(self.nombre.valeur))
#        disp_valeur.insert(0, self.nombre.valeur)
        disp_valeur.pack(side = RIGHT, expand = True)
        disp_valeur.bind("<Return>", self.update_valeur)

        frame2 = Frame(self, relief = RAISED, borderwidth = 1)
        frame2.pack(fill = BOTH)
        label2 = Label(frame2, text = "Base")
        self.base = StringVar()
        label2.pack(side = LEFT)
        disp_base = Entry(frame2, textvar = self.base)
        disp_base.delete(0, END)
        self.base.set(self.nombre.base)
#        disp_base.insert(0, self.nombre.base)
        disp_base.pack(side = RIGHT, expand=True)
        disp_base.bind("<Return>", self.update_base)


        frame3 = Frame(self, relief=RAISED, borderwidth=1)
        frame3.pack(fill=BOTH)
        self.ecriture = StringVar()
        label3 = Label(frame3, text="Ecriture")
        label3.pack(side=LEFT)
        disp_ecriture = Entry(frame3, textvar = self.ecriture)
        disp_ecriture.delete(0, END)
        self.ecriture.set(self.nombre.represente())
#        disp_base.insert(0, self.nombre.represente())
        disp_ecriture.pack(side=RIGHT, expand=True)
        disp_ecriture.bind("<Return>", self.update_ecriture)

    def update_valeur(self, event):
        self.nombre.valeur = int(self.valeur.get())
        self.ecriture.set(self.nombre.represente())
        print("updated")

    def update_base(self, event):
        self.nombre.base = int(self.base.get())
        self.ecriture.set(self.nombre.represente())
        print("updated")

    def update_ecriture(self, event):
        self.nombre.update_valeur(str(self.ecriture.get()))
        self.valeur.set(str(self.nombre.valeur))


def main():
    racine = Tk()
    racine.geometry("250x150+300+300")
    app = Convertisseur()
    racine.mainloop()

main()