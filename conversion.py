class Nombre():
    def __init__(self, valeur = 0, base = 10):
        self.valeur = valeur
        self.base = base
        self.represente()

    def represente(self):
        chiffres_total = "0123456789abcdefghijklmnopqrstuvwxyz"
        B = self.base
        chiffres = {}
        for c in range(B):
            chiffres[c] = chiffres_total[c]
        n = self.valeur
        repr = ""
        while (n // B) != 0:
            reste = n % B
            repr = chiffres[reste]+repr
            n = n // B
        repr = chiffres[n]+repr
        print(repr)
        return repr

    def update_valeur(self, representation):
        B = self.base
        chiffres_total = "0123456789abcdefghijklmnopqrstuvwxyz"
        chiffres = {}
        for c in range(B):
            chiffres[chiffres_total[c]] = c
        val = 0
        for car in representation:
            val = B*val+chiffres[car]
        self.valeur = val


def main():
    nombre = Nombre()
    commande = ""

    while commande != "quit" and commande !="exit":
        print(f"Valeur : {nombre.valeur}  Base : {nombre.base}  Représentation : {nombre.represente()}")
        prompteur = "Entrez v pour valeur, b pour base , r pour représentation et exit pour quitter : "
        print()
        commande = input(prompteur)
        if commande == "v":
            nombre.valeur = int(input("valeur "))
        elif commande == "b":
            nombre.base = int(input("Base "))
        elif commande == "r":
            representation = input("Représentation ")
            nombre.update_valeur(representation)
        elif commande in {"quit", "exit"}:
            break


if __name__ == "__main__":
    main()


