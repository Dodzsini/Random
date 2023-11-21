import json

with open("database.json", "r", encoding="utf8")as fajl:
    adatbazis=json.loads(fajl)

print(adatbazis)
