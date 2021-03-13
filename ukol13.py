class Cars:
    def __init__(self, SPZ, znacka, km):
        self.SPZ = SPZ
        self.znacka = znacka
        self.km = km
        self.kdispozici = True
        self.pocet_najetych_km = km

    def dostupnost(self):
        self.kdispozici = False

    def getInfo(self):
        return f"Registrační značka vozidla je {self.SPZ}, značka a typ vozidla je {self.znacka} a najelo celkem {self.km}."

    def pujc_auto(self):
        if self.kdispozici:
            peugeot.dostupnost()
            octavia.dostupnost()
            print("Automobil je volný.")
        else:
            print("Automobil je půjčený.")

    def vrat_auto(self, km, pocet_pujcenych_dni):
        if self.pocet_najetych_km <= km:
            self.pocet_najetych_km += km
        if pocet_pujcenych_dni < 7:
            celkova_cena = pocet_pujcenych_dni * 400
            return f"Cena za půjčení auta je {celkova_cena} Kč za {pocet_pujcenych_dni} dní."
        else:
            celkova_cena = pocet_pujcenych_dni * 300
            return f"Cena za půjčení auta je {celkova_cena} Kč za {pocet_pujcenych_dni} dní."

peugeot = Cars("4A2 3020", "Peugeot 403 Cabrio", "47534")
octavia = Cars ("1P3 4747", "Škoda Octavia", "41253")

pocet_pujcenych_dni = int(input("Kolik dní jste měl auto půjčené? "))
pocet_najetych_km = input("Kolik km jste s autem najel? ")
print(pocet_pujcenych_dni.vrat_auto())

#celkova_cena = pocet_pujcenych_dni
#if pocet_pujcenych_dni < 7:
#   celkova_cena = pocet_pujcenych_dni * 400
#   print(f"Cena za půjčení auta je {celkova_cena} Kč za {pocet_pujcenych_dni} dní.")
#else:
#   celkova_cena = pocet_pujcenych_dni * 300
#   print(f"Cena za půjčení auta je {celkova_cena} Kč za {pocet_pujcenych_dni} dní.")

print(peugeot.getInfo())
print(octavia.getInfo())

