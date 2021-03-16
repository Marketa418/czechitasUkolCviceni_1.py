from datetime import datetime, timedelta

datum = input("Uveďte datum, kdy chcete jít do kina: ")
pocet_osob = int(input("Pro kolik osob chcete lístky: "))
datum_novy = datetime.strptime(datum, "%d. %m. %Y")

start_hlavni_sezona = datetime(2021, 7, 1)
konec_hlavni_seozna = datetime(2021, 8, 10)
start_vedlejsi_sezona = datetime(2021, 8, 11)
konec_vedlejsi_seozna = datetime(2021, 8, 31)

if start_hlavni_sezona <= datum_novy <= konec_hlavni_seozna:
  cena_za_listky = pocet_osob * 250
  print(f"Cena za vstupenky je {cena_za_listky}.")
elif start_vedlejsi_sezona <= datum_novy <= konec_vedlejsi_seozna:
  cena_za_listky = pocet_osob * 180
  print(f"Cena za vstupenky je {cena_za_listky}.")
else:
  print("Kino není otevřené.")


