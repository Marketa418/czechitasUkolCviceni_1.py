def total_points(odvetvi, obrat, zeme, konference = False, newsletter = False):
  obrat = int(obrat)
  if odvetvi == "automotive":
    point =+ 3
  elif odvetvi == "retail":
    point =+ 2
  else:
    point =+ 0
  if obrat <= 10000000:
    point =+ 0
  elif obrat > 10000000:
    point =+ 3
  else:
    point =+ 1
  if zeme in ["Česká republika", "Slovensko"]:
    point =+ 2
  elif zeme in ["Německo" or "Francie"]:
    point =+ 1
  else:
    point = 0
  if konference:
    point = 1
  if newsletter:
    point = 1
  point = int(point)
  point = sum(point)
  return point

odvetvi = input("Zadejte Vámi prováděné odvětví.")
obrat = int(input("Zadejte obrat:"))
zeme = input("Vložete zemi v jaké podnikáte: ")
konference = input("Pořádáte konference? Pokud ne, tak nevyplňujte kolonku. ")
newsletter = input("Posíláte newslettery? Pokud ne, tak nevyplňujte kolonku.")

point = total_points(odvetvi, obrat, zeme, konference = False, newsletter = False)
if point <= 5:
  print ("Malá šance na úspěch.")
elif point > 6:
  print ("Střední šance na úspěch.")
elif point <= 8:
  print ("Střední šance na úspěch.")
else:
  print("Šance na úspěch je vysoká.")
