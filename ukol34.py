import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/7/velikonoce.csv")
import pandas
import matplotlib.pyplot as plt
velikonoce = pandas.read_csv("velikonoce.csv")
#Vytvoř sloupcový graf, který data přehledně zobrazí.
#Na ose x budou vidět jednotlivá data ("datumy") a výška sloupce označí, kolikrát na daný den připadly Velikonoce.
#velikonoce.plot.bar(x="Datum", y="Počet")

ax = velikonoce.plot.bar(x="Datum", y="Počet", title = "Počet Velikonoc v určitých dnech v období 1600-2100", ylim = (3, 24))
ax.set_ylabel("Počet Velikonoc")
ax.set_xlabel("Datumy")
plt.show()


