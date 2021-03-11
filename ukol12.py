class Cars:
    def __init__(self, SPZ, znacka, km):
        self.SPZ = SPZ
        self.znacka = znacka
        self.km = km
        self.kdispozici = True

    def dostupnost(self):
        self.kdispozici = False

    def getInfo(self):
        return f"Registrační značka vozidla je {self.SPZ}, značka a typ vozidla je {self.znacka}."

    def pujc_auto(self):
        if self.kdispozici:
            peugeot.dostupnost()
            octavia.dostupnost()
            print("Automobil je volný.")
        else:
            print("Automobil je půjčený.")

peugeot = Cars("4A2 3020", "Peugeot 403 Cabrio", "47534")
octavia = Cars ("1P3 4747", "Škoda Octavia", "41253")

jake_auto_chcete_pujcit = input("Jaké auto si přejete půjčit? Peugeot/Octavia ")
if "Peugeot" in jake_auto_chcete_pujcit:
    print(peugeot.getInfo())
    print(peugeot.pujc_auto())
else:
    print(octavia.getInfo())
    print(octavia.pujc_auto())



jake_auto_chcete_pujcit = input("Jaké auto si přejete půjčit? Peugeot/Octavia ")
if "Peugeot" in jake_auto_chcete_pujcit:
    print(peugeot.getInfo())
    print(peugeot.pujc_auto())
else:
    print(octavia.getInfo())
    print(octavia.pujc_auto())