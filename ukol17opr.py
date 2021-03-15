class Polozka:
    def __init__(self, nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr

class Film(Polozka):
    def __init__(self, nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka = delka

    def get_Info(self):
        return f"Název filmu je {self.nazev} a žánr je {self.zanr}. Délka filmu je {self.delka} min."

    def get_celkova_delka(self):
        return self.delka

class Serial(Polozka):
    def __init__(self, nazev, zanr, pocet_epizod, delka_epizody):
        super().__init__(nazev, zanr)
        self.pocet_epizod = pocet_epizod
        self.delka_epizody = delka_epizody

    def get_Info(self):
        return f"Název seriálu je {self.nazev} a žánr je {self.zanr}. Počet epizod je {self.pocet_epizod} a délka jedné epizody je {self.delka_epizody} min."

    def get_celkova_delka(self):
        celkova_delka_serialu = self.pocet_epizod  * self.delka_epizody
        return celkova_delka_serialu

class Uzivatel:
    def __init__(self, uzivatelske_jmeno, delka_sledovani):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.delka_sledovani = 0

    def pripocti_zhlednuti(self, celkova_delka_serialu):
        self.delka_sledovani += celkova_delka_serialu
        return self.delka_sledovani

nepritel_pred_branami = Film("Nepřítel před branami", "válečné/drama", 280)
hnizdo = Serial("Hnízdo", "drama", 10, 60)
karel = Uzivatel("Karel", 0)


print(nepritel_pred_branami.get_Info())
print(hnizdo.get_Info())
print(hnizdo.get_celkova_delka())
print(nepritel_pred_branami.get_celkova_delka())
print(karel.pripocti_zhlednuti(hnizdo.get_celkova_delka()))
print(karel.pripocti_zhlednuti(nepritel_pred_branami.get_celkova_delka()))