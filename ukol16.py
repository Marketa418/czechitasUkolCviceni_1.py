class Polozka:
    def __init__(self, nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr

class Film(Polozka):
    def __init__(self, nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka = delka

    def get_Info(self):
        return f"Název filmu je {self.nazev}, žánr je {self.zanr} a délka je {self.delka} min."


class Serial(Polozka):
    def __init__(self, nazev, zanr, pocet_epizod, delka_epizody):
        super().__init__(nazev, zanr)
        self.pocet_epizod = pocet_epizod
        self.delka_epizody = delka_epizody

    def get_Info(self):
        return f"Název seriálu je {self.nazev} a žánr je {self.zanr}. Počet epizod je {self.pocet_epizod} a délka jedné epizody je {self.delka_epizody} min."

nepritel_pred_branami = Film("Nepřítel před branami", "válečné/drama", 280)
hnizdo = Serial("Hnízdo", "drama", 10, 60)

print(nepritel_pred_branami.get_Info())
print(hnizdo.get_Info())