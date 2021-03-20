import pandas
import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv")
country_vaccinations = pandas.read_csv('country_vaccinations.csv')
country_vaccinations = country_vaccinations.set_index("country")
#1) Dotaz na počty očkovaných (sloupec total_vaccinations) v jednotlivých státech dne 2021-03-10 (s datem pracuj úplně stejně jako s řetězcem, tj. nevyužívej modeul datetime, ale vlož do dotazu přímo řetězec).
pocet_ockovanych_2021_03_10 = country_vaccinations[(country_vaccinations["date"] == "2021-03-10")]
print(pocet_ockovanych_2021_03_10[["date", "total_vaccinations"]])

#2) Dotaz na řádky, kde 2021-03-10 bylo naočkováno více než 1 mil. obyvatel.
meloun_naocko = country_vaccinations[(country_vaccinations["date"] == "2021-03-10") & (country_vaccinations["total_vaccinations"] > 1000000)]
print(meloun_naocko[["date", "total_vaccinations"]])

#3) Podíváme se na extrémní hodnoty. Napiš dotaz na řádky, kde za daný den naočkování více než 100 tisíc lidí nebo naopak méně než 100 lidí.
max_a_min_daily = country_vaccinations[(country_vaccinations["daily_vaccinations"] > 100_000) | (country_vaccinations["daily_vaccinations"] < 100)]
print(max_a_min_daily[["date", "daily_vaccinations"]])

# Bonus: Vypiš informace o očkování za dny 2021-03-10 a 2021-03-11 pro státy United Kingdom, Finland a Italy. Použij např. funkci isin().
u_f_i = country_vaccinations.loc[["Finland", "Italy", "United Kingdom"]]
u_f_i_dates = u_f_i[u_f_i["date"].isin(["2021-03-10", "2021-03-11"])]
print(u_f_i_dates)

#Vypiš informace o očkování pro Japan mezi daty 2021-03-03 a 2021-03-09. Data v tomto formátu můžeš porovnávat pomocí operátorů >= a <= jako řetězce, tj. opět nemusíš použít modul datetime.
japan = country_vaccinations.loc[["Japan"]]
japan_dates = japan[(japan["date"] >= "2021-03-03") & (japan["date"] <= "2021-03-09")]
print(japan_dates)