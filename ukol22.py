import pandas
import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv")

zemrele_postavy = pandas.read_csv('character-deaths.csv')
zemrele_postavy = zemrele_postavy.set_index("Name")

print(zemrele_postavy.columns)

#3) Použij funkci loc ke zjištění informací o smrti postavy jménem "Hali"
print(zemrele_postavy.loc[["Hali"]])

#4) Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam".
print(zemrele_postavy["Gevin Harlaw":"Gillam"])

#5) Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a sloupce Death Year.
print(zemrele_postavy.loc["Gevin Harlaw":"Gillam", "Death Year"])

#6) Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a informace o tom, v jakých knihách se postava vyskytuje, tj. vypiš všechny sloupce mezi GoT a DwD.
print(zemrele_postavy.loc["Gevin Harlaw":"Gillam", "GoT":"DwD"])
