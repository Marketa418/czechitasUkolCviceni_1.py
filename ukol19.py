from forex_python.converter import CurrencyRates
prevodnik = CurrencyRates()
pozadovana_mena = input("Jakou měnu si přejete vyměnit? EUR, GBP, DKK ")
pozadovano_v_cilove_mene = int(input("Kolik požadujete v cílové měně? "))
cena_v_korunach = prevodnik.convert(pozadovana_mena, 'CZK', pozadovano_v_cilove_mene)

print(cena_v_korunach)

