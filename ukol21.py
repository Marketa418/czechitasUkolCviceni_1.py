import pandas
import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

twlo = pandas.read_csv('twlo.csv')


#1)
pocet_radku = print(twlo.shape[0])
#2)
pocet_sloupcu = print(twlo.shape[1])
#3)
nejnovejsi_cena = print(twlo.iloc[301])
#4)
pet_radku_s_cenami = print(twlo.iloc[0:5])
fce_head = print(twlo.head(5))

#Dobrovolný úkol
procentni_zmena_ceny = round(twlo.iloc[0,5]/twlo.iloc[301,5] * 100)
print(f"Procentní změna je {procentni_zmena_ceny}%.")
price_range = (twlo.iloc[:,2])
nejvyssi_hodnota = max(price_range)
nejnizsi_hodnota = round(min(price_range))
print (f"Price range je od {nejnizsi_hodnota}Kč do {nejvyssi_hodnota}Kč.")



