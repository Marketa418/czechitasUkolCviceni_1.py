import wget
import pandas
#wget.download("https://data.mpsv.cz/od/soubory/volna-mista/volna-mista.json")
volna_mista = pandas.read_json("volna-mista.json")
#volna_mista_chtena = (volna_mista[volna_mista["cizinecMimoEu"]] == True)
#print(volna_mista_chtena)
#print(volna_mista.columns)



