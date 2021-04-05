import pandas
import matplotlib.pyplot as plt

twilio = pandas.read_csv("twlo.csv")
#twilio = pandas.Series("twlo")
twilio.plot(x= "Date", y="Close")
plt.show()

twilio["Date"] = pandas.to_datetime(twilio["Date"])
twilio.plot(x= "Date", y="Close")
plt.show()

#Dobrovolný úkol
ax = twilio.plot(x= "Date", y="Close")
ax.set_ylabel("Cena v dolarech")
ax.set_xlabel("Datum")
plt.show()