number = input("Zadejte telefonní číslo, kam chcete SMS poslat: ")
number = number.replace(" ", "")
if len(number) == 9:
  print(True)
elif len(number) ==13:
  if "+" in number:
    print (True)
else:
  print (False)

if len(number) == 9:
  text = input("Zde napište text: ")
elif len(number) ==13:
  if "+" in number:
    text = input("Zde napište text: ")
else:
  False

  numberOfText = 0
  for znak in text:
    if znak in "aábcdeéfghiíjklmnňoópqrřsštťuúůvwxyýzž":
      numberOfText = int(numberOfText)
      numberOfText = numberOfText + 1
      if numberOfText < 180:
        totalPriceSms = 3 * 1
        print(f"Cena za SMS je {totalPriceSms}")
      else:
        totalPriceSms = 3 * 2
        print(f"Cena za SMS je {totalPriceSms}")