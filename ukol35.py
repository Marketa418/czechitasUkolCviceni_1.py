import pandas
import matplotlib.pyplot as plt

temperature = pandas.read_csv("temperature.csv")
#Vytvoř tabulku, která bude obsahovat údaje o teplotě za města Helsinki, Miami Beach a Tokyo.
#print(temperature)
helsinki_miami_tokyo = temperature[temperature["City"].isin(["Helsinki", "Miami Beach", "Tokyo"])]
print(helsinki_miami_tokyo)

#Vytvoř krabicový graf a porovnej rozsah teplot v těchto městech.
#helsinki_miami_tokyo("AvgTemperature")[["Miami Beach", "Helsinki", "Tokyo"]].plot()
#plt.show()

ax = helsinki_miami_tokyo.boxplot(column="AvgTemperature", by="City", figsize=(10, 10))
ax.set_ylabel("Průměrná teplota v F")
ax.set_xlabel("Výběr měst")
ax.set_title("Průměrná teplota ve vybraných městech ve F")
plt.show()