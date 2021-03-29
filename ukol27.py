import wget
import pandas

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/vykazy.csv")

#1)
vykazy = pandas.read_csv("vykazy.csv")
print(vykazy)

#2)
print(vykazy.groupby('project')[["hours"]].sum())

#bonusový úkol
zam_praha = pandas.read_csv("zam_praha.csv")
zam_plzen = pandas.read_csv("zam_plzeň.csv")
zam_liberec = pandas.read_csv("zam_liberec.csv")
platy_2021_02 = pandas.read_csv("platy_2021_02.csv")

zam_praha["město"] = "Praha"
zam_plzen["město"] = "Plzeň"
zam_liberec["město"] = "Liberec"

zamestnanci = pandas.concat([zam_praha, zam_plzen, zam_liberec], ignore_index=True)
vykazy = vykazy.rename(columns={"emloyee_id" : "cislo_zamestnance"})
vykazy_zamestanci = pandas.merge(zamestnanci, vykazy, on=["cislo_zamestnance"])
#print(vykazy_zamestanci)
print(vykazy_zamestanci.groupby(["město", "project"])[["hours",]].sum())

