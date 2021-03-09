number = input("Zadejte telefonní číslo, kam chcete SMS poslat: ")
number = number.replace(" ", "")
if len(number) == 9:
    print(True)
elif len(number) == 13:
    if "+" in number:
        print(True)
else:
    print(False)

if len(number) == 9:
    text = input("Zde napište text: ")
elif len(number) == 13:
    if "+" in number:
        text = input("Zde napište text: ")
else:
    print("Neplatné číslo.")
    exit()

numberOfText = 0
for znak in text:
    if not znak in "aábcdeéfghiíjklmnňoópqrřsštťuúůvwxyýzž ":
        print("Neplatný znak ve zprávě")
        exit()

numberOfText = int(len(text) / 180 + 1)
totalPriceSms = numberOfText * 3
print(f"Cena za SMS je {totalPriceSms} Kč")