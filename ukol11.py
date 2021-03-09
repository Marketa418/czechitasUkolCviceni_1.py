class Cars:
  def __init__(self, SPZ, znacka, km):
    self.SPZ = SPZ
    self.znacka = znacka
    self.km = km
    self.kdispozici = True

  def dostupnost(self):
    self.kdispozici = False

  def getInfo(self):
    if self.kdispozici:
      return f"Registrační značka vozidla je {self.SPZ}, značka a typ vozidla je {self.znacka} má najeto {self.km} a je k dispozici."
    return f"Registrační značka vozidla je {self.SPZ}, značka a typ vozidla je {self.znacka} má najeto {self.km} a není k dispozici."



peugeot = Cars("4A2 3020", "Peugeot 403 Cabrio", "47534")
octavia = Cars ("1P3 4747", "Škoda Octavia", "41253")

print(peugeot.getInfo())
print(peugeot.getInfo())