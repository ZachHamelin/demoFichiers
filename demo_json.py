import json

dict_ventes = {}

with open("ventes.json", "r", encoding="utf-8") as inventaire:
    dict_ventes = json.load(inventaire)

print(dict_ventes)
print(len(dict_ventes))
print(sum(dict_ventes.values()))