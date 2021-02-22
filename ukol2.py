sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
kodSoucastky = input ("Zadej kód součástky: ")
mnozstviSoucastky = input ("Jaké množství si přejete? ")
mnozstviSoucastky = int(mnozstviSoucastky)
if kodSoucastky in sklad:
  if sklad[kodSoucastky] < mnozstviSoucastky:
    print ("Součástka je v nižším množství, než požadujete.")
    sklad[kodSoucastky] = sklad[kodSoucastky] - sklad[kodSoucastky]
  else:
    print ("Vaše objednávka bude uspokojena.")
    sklad[kodSoucastky] = sklad[kodSoucastky] - mnozstviSoucastky
else:
  print ("Součástka není skladem.")
print (sklad)