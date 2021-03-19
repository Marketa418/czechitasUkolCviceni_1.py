from datetime import datetime, timedelta

class Kontakt:
  def __init__(self, jmeno, email):
    self.jmeno = jmeno
    self.email = email

class Uchazec (Kontakt):
    def __init__(self, jmeno, email, datum_pohovoru, zapis_z_pohovoru = ""):
        super().__init__(jmeno, email)
        self.datum_pohovoru = datum_pohovoru
        self.zapis_z_pohovoru = zapis_z_pohovoru

    def pridej_zapis(self, zapis_z_pohovoru):
        self.datum_pohovoru = datetime.strptime(self.datum_pohovoru,"%d. %m. %Y")
        if datetime.now() < self.datum_pohovoru:
            print("Pohovor ještě neproběhl.")
        else:
            self.zapis_z_pohovoru += zapis_z_pohovoru
            print(f"Zápis byl uložen. Zápis z pohovoru je {self.zapis_z_pohovoru}")

    def get_Info(self):
        return f"Jméno nového uchazeče je {self.jmeno}, jeho email je {self.email} na pohovor přišel dne {self.datum_pohovoru}. Zápis z pohovoru je: {zapis_z_pohovoru}."

pepa = Uchazec("Pepa urbanec", "pepa.urbanec.seznam.cz", "26. 2. 2021")
martin = Uchazec("Martin Straka", "martin.straka.gmail.com", "5. 4. 2021")
alena = Uchazec("Alena Mánesová", "alenka.z.rise.divu.com", "3. 3. 2021")
print(pepa.pridej_zapis("Pepa byl dokonalý uchazeč."))
print(martin.pridej_zapis(""))
print(alena.pridej_zapis("Umí komunikovat s lidmi."))