import matplotlib.pyplot as plt
import pandas
#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")
platy = pandas.read_csv("platy_2021_02.csv")

#Načti si tato data do tabulky a vytvoř histogram.
#Nastav vhodně hranice skupin histogramu (parametr bins), aby byl graf přehledný a snadno interpretovatelný.
tabulka_jen_plat = platy[["plat"]]
print(tabulka_jen_plat)
tabulka_jen_plat.hist(bins=[30000, 32000, 34000, 36000, 38000, 40000, 42000 ,44000, 46000, 48000, 50000, 52000, 54000, 56000, 58000, 60000])
plt.show()

#Bonus
#1) načti data
zam_praha = pandas.read_csv("zam_praha.csv")
zam_plzen = pandas.read_csv("zam_plzeň.csv")
zam_liberec = pandas.read_csv("zam_liberec.csv")
platy_2021_02 = pandas.read_csv("platy_2021_02.csv")

zam_praha["město"] = "Praha"
zam_plzen["město"] = "Plzeň"
zam_liberec["město"] = "Liberec"

#2) vytvoř novou tabulku zaměstnanci
zamestnanci = pandas.concat([zam_praha, zam_plzen, zam_liberec], ignore_index=True)
#print(zamestnanci)
#3) propojení tabulky zamestnanci a platy_zamestancnu
platy_zamestnancu = pandas.merge(platy_2021_02, zamestnanci, on=['cislo_zamestnance'])
jen_sloupecek_s_platy_zamestnanu = platy_zamestnancu[["plat", "město"]]
jen_sloupecek_s_platy_zamestnanu.hist(by="město")
plt.show()


