import pandas
import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

temperature = pandas.read_csv('temperature.csv')
temperature = temperature.set_index("City")


print(temperature.iloc[2:5])

#1) Dotaz na měření, která byla provedena v Praze. Je na datech něco zvláštního? Napadá tě, čím to může být? Zde je nápověda.
print(temperature.loc[["Prague"]])

#2) Dotaz na měření, ve kterých je teplota (sloupec AvgTemperature) vyšší než 80 stupňů.
avg_80 = (temperature[temperature["AvgTemperature"] > 80])
print(avg_80)

#3) Dotaz na měření, ve kterých je teplota vyšší než 60 stupňů a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).
avg_60_EU = temperature[(temperature["AvgTemperature"] > 60) & (temperature["Region"] == "Europe")]
print(avg_60_EU)

#4) Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 80 stupňů nebo menší než - 20 stupňů.
avg_80_20 = temperature[(temperature["AvgTemperature"] > 80) | (temperature["AvgTemperature"] < -20)]
print(avg_80_20[["Country", "Region", "AvgTemperature"]])