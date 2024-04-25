from fastapi import FastAPI
from pymongo import MongoClient
from Musique_class import Musique
from Magasin_class import Magasin

app = FastAPI()

client = MongoClient(host="mongodb")

db = client["mabase"]
col = db["musique"]

@app.get("/musique", response_model=list[Musique])
def get_musique():
    musique = col.find()
    return list(musique)

@app.post("/add_musique")
def add_musique(musique : Musique):
    col.insert_one(musique.model_dump()).inserted_id
    return musique

@app.get("/magasin" , response_model=list[Magasin])
def get_magasin():
    magasin = col.find()
    return list(magasin)

@app.post("/add_magasin")
def add_magasin(magasin : Magasin):
    col.insert_one(magasin.model_dump()).inserted_id
    return magasin
