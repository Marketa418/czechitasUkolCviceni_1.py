baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
kodBaliku = input ("Zadejte číslo balíku: ")
if kodBaliku in baliky:
  if baliky[kodBaliku] == True:
    print ("Balík je na cestě.")
  else:
    print ("Balík není na cestě.")
else:
    print ("Balík není na cestě")