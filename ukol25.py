import pandas
import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

temperature = pandas.read_csv('temperature.csv')
temperature = temperature.set_index("City")

#Vypiš si prvních několik řádků, ať si prohlédneš strukturu tabulky. Dále napiš následující dotazy:
#print(temperature.iloc[0:6])

#1) Dotaz na řádky z 13. listopadu 2017 (sloupec Day musí mít hodnotu 13).
trinacteho_listopadu = temperature[temperature["Day"] == 13]
print(trinacteho_listopadu)

#2) Dotaz na řádky z 13. listopadu 2017 ze Spojených států amerických (sloupec Day musí mít hodnotu 13 a sloupec Country hodnotu US). Výsledek dotazu si ulož do nové tabulky a použij ji jako vstup pro následující dotaz.
trinacteho_listopadu_US = (temperature[(temperature["Day"] == 13) & (temperature["Country"] == "US")])
print(trinacteho_listopadu_US)

#3) Pro data z předchozího dotazu napiš dotaz na řádky ve městech (sloupec City) Washington a Philadelphia.
##print(trinacteho_listopadu_US[trinacteho_listopadu_US["City"].isin(["Washington", "Philadelphia"])]) - toto jde bez klíče
##print(trinacteho_listopadu_US.loc["Philadelphia"]) - toto jde jen když klíč, index je nastaven na City
print(trinacteho_listopadu_US.loc[["Washington", "Philadelphia"]])

#dobrovolný úkol
trinacteho_listopadu_US = (temperature[(temperature["Day"] == 13) & (temperature["Country"] == "US")])
print(trinacteho_listopadu_US["AvgTemperature"].mean())
print(trinacteho_listopadu_US["AvgTemperature"].median())
print(trinacteho_listopadu_US["AvgTemperature"].var())
