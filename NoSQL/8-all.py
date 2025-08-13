#!/usr/bin/env python3
from pymongo import MongoClient
def list_all(mongo_collection):
    # Connexion à MongoDB (par défaut localhost:27017)
    client = MongoClient()

    # Sélection de la base de données
    db = client.my_db

    # Sélection de la collection
    collection = db.school

    # Lister tous les documents
    for document in collection.find():
        print(document)
