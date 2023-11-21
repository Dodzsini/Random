import json

<<<<<<< HEAD
adatbazis=[]


#hoppakupon
with open("database.json", "r", encoding="utf8")as fajl:
    adatbazis=json.load(fajl)
=======
with open("database.json", "r", encoding="utf8")as fajl:
    adatbazis=json.loads(fajl)
>>>>>>> a094fb8f67f4e6e411629620845d37a69700f264

print(adatbazis)
