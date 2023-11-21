import json

adatbazis=[]


#hoppakupon
with open("database.json", "r", encoding="utf8")as fajl:
    adatbazis=json.load(fajl)

print(adatbazis)
