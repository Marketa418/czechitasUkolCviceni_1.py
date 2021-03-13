from faker import Faker

class Balik:
  def get_info(self):
    print(f"Příjemce balíku: {self.name}")
    print(f"Balík doručte na adresu: {self.address}")

  def __init__(self, name, address):
    self.name = name
    self.address = address

generator_falesnych_dat = Faker("cs_CZ")
zakaznik = Balik(generator_falesnych_dat.name(), generator_falesnych_dat.address())
zakaznik2 = Balik(generator_falesnych_dat.name(), generator_falesnych_dat.address())

print(zakaznik.get_info())
print(zakaznik2.get_info())


