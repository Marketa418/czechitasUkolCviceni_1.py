import wget
import pandas
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
temperature = pandas.read_csv("temperature.csv")

#1) Vyfiltruj si informace o teplotách 13. listopadu 2017.
temperature_13 = temperature[temperature["Day"] == 13]
print(temperature_13)

#2) Vyřaď všechny záznamy, které mají teplotu -99, protože tato hodnota je pravděpodobně chybná.
temperature_without_99 = temperature[temperature["AvgTemperature"] > -99]
print(temperature_without_99)

#3) Vypočti počet dat, které máš pro daný den za jednotlivé regiony.
print(temperature.groupby('Region')['Day'].count())

#4) Vypočti průměrnou teplotu za jednotlivé regiony.
print(temperature_without_99.groupby('Region')['AvgTemperature'].mean())

#5) Vypočti maximální a minimální teplotu v každém regionu.
print(temperature_without_99.groupby('Region')['AvgTemperature'].max())
print(temperature_without_99.groupby('Region')['AvgTemperature'].min())