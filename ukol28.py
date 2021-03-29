import pandas
import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/staty.json")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/gdp.csv")

#1) načti data
staty = pandas.read_json("staty.json")
print(staty)

#2) Vyfiltruj státy, které leží v Evropě.
staty_v_Evrope = (staty[staty["region"] == "Europe"])
print(staty_v_Evrope[["name"]])

#3) Zjisti počet států v jednotlivých subregionech Evropy.
print(staty.groupby("subregion")[["name"]].count())

#4) Zjisti cekový počet obyvatel v jednotlivých subregionech Evropy.
print(staty.groupby("subregion")[["population"]].sum())

#Bonus
#wget.download("https://github.com/pesikj/python-012021/blob/master/zadani/6/gdp.csv")
gdp = pandas.read_csv("gdp.csv")
#Načti informace ze souborů do tabulek. Z tabulky s GDP odeber státy, které nemají kompletní informace GDP (tj. ponech pouze státy, které mají kompletní data za všechny tři roky).
#print(gdp.shape)
#print(len(gdp[gdp["2019"].isnull()]))
#print(len(gdp[gdp["2018"].isnull()]))
#print(len(gdp[gdp["2017"].isnull()]))

gdp = pandas.read_csv("gdp.csv").dropna()
print(len(gdp[gdp["2019"].isnull()]))
print(len(gdp[gdp["2018"].isnull()]))
print(len(gdp[gdp["2017"].isnull()]))
print(gdp.shape)

#Propoj obě tabulky podle třípísmenného kódu států.
staty = staty.rename(columns={"alpha3Code" : "Country Code"})
staty_gdp = pandas.merge(staty, gdp, on=["Country Code"], how="right")
#print(staty_gdp)

#Spočti celkové HDP za rok 2019 a celkový počet obyvatel za jednotlivé subregiony.
new_table = staty_gdp.groupby("subregion")[["2019", "population"]].sum()

#K tabulce, kterou jsi vytovřila v předchozím kroku,
#vypočti GDP v roce 2019 na obyvatele, tj. přidej sloupec s velikostí GDP v roce 2019 vydělenou počtem obyvatel daného subregionu.
new_table["gdp/population"] = new_table["2019"] / new_table["population"]
print(new_table)