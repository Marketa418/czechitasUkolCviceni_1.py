#import wget
import pandas

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")

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
#platy_zamestnancu = pandas.merge(zamestnanci, platy_2021_02, on=['cislo_zamestnance'])
platy_zamestnancu = pandas.merge(platy_2021_02, zamestnanci, on=['cislo_zamestnance'])
#print(platy_zamestnancu)

#4) porovnání tabulek před a po spojení
print(zamestnanci.shape)
print(platy_zamestnancu.shape)

#5) Spočti průměrný plat zaměstnanců v jednotlivých kancelářích
#print(platy_zamestnancu.groupby('město')[["plat"]].mean())

#Bonus
#Ulož do proměnné počet zaměstnaců, kteří v naší firmě již nepracují.
nepracujici_2021_02 = 13
#V rámci úspory se IT oddělení rozhodlo prověřit licence přidělené zaměstnancům, kteří ve firmě již nepracují. Vytvoř samostatnou tabulku, která obsahuje jména zaměstnanců, kteří ve firmě již nepracují.
# Tabulku ulož do souboru CSV.
platy_zamestnancu = pandas.merge(platy_2021_02, zamestnanci, on=['cislo_zamestnance'], how="outer")
nepracujici_2021_02_jmenne = platy_zamestnancu[platy_zamestnancu["plat"].isnull()]
print(nepracujici_2021_02_jmenne)
nepracujici_2021_02_jmenne.to_csv("nepracujici_2021_02_jmenne.csv")









