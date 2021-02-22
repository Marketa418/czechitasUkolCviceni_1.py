prodeje2019 = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

prodeje2020 = {
    "Zkus mě chytit": 3157,
    "Vrah zavolá v deset": 3541,
    "Vražda podle knihy": 2510,
    "Past": 2364,
    "Zločinný steh": 5412,
    "Zkus mě chytit": 6671,
}
prodejKnihy = input ("Pro jaký název knihy chcete znát tržby? ")
if prodejKnihy not in prodeje2019:
  prodeje2019[prodejKnihy] = 0
trzbaZaKnihu = prodeje2019[prodejKnihy]+prodeje2020[prodejKnihy]
print (f"Celkem je tržba {trzbaZaKnihu}Kč za knihu {prodejKnihy}.")