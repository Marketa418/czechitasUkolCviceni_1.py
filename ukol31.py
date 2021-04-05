import pandas
#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
temperature = pandas.read_csv("temperature.csv")

#1) Vyfiltruj si informace o teplotách 13. listopadu 2017.
temperature_13 = temperature[temperature["Day"] == 13]
print(temperature_13)

#2) Vyřaď všechny záznamy, které mají teplotu -99, protože tato hodnota je pravděpodobně chybná.
temperature_without_99 = temperature[temperature["AvgTemperature"] > -99]
print(temperature_without_99)

#3)Seřad hodnoty v souboru podle teploty od největší po nejmenší.
temperature_without_99_serazene = temperature_without_99.sort_values(by="AvgTemperature", ascending=False)
print(temperature_without_99_serazene)

#4)Vypiš pět měst s nejvyšší teplotou a pět měst s nejnižší teplotou.
print(temperature_without_99_serazene.iloc[0:5])
print(temperature_without_99_serazene.iloc[-5:])

