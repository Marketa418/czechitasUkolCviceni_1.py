vysledky = [
  {"Jméno": "Mirek Dušín", "Český jazyk": 1, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 1, "Zeměpis": 1},
  {"Jméno": "Jarka Metelka", "Český jazyk": 3, "Anglický jazyk": 1, "Matematika": 3, "Dějepis": 2, "Ekonomika": 5},
  {"Jméno": "Jindra Hojer", "Český jazyk": 2, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 3, "Chemie": 3},
  {"Jméno": "Červenáček", "Český jazyk": 1, "Anglický jazyk": 1, "Matematika": 1, "Fyzika": 2, "Informatika": 4},
  {"Jméno": "Rychlonožka", "Český jazyk": 4, "Anglický jazyk": 3, "Matematika": 2, "Chemie": 1, "Biologie": 4},
]


def ohodnot_studenta(radek):

  average = sum(radek) / 5

  if average <= 1.5:

    if 3 not in radek:

      print("Prospěl s vyznamenáním.")

    else:

      print("Prospěl")

  elif 5 in radek:

    print("Neprospěl.")

  else:

    print("Prospěl.")

  return average



for radek in vysledky:

  jmeno_studenta = radek.pop("Jméno")

  print(jmeno_studenta, end=": ")

  ohodnot_studenta(radek.values())
