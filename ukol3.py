volnePokoje = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]
}

cisloHodiny = input("V kolik hodin si chcete zarezervovat meeting room?")
cisloHodiny = int(cisloHodiny)
print (len(volnePokoje[cisloHodiny]))