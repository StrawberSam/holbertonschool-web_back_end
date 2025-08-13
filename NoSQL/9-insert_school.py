#!/usr/bin/env python3
"""
Module insert_school
Ce module contient une fonction permettant d'insérer un nouveau document
dans une collection MongoDB en utilisant PyMongo.
"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Insère un nouveau document dans la collection MongoDB.

    Args:
        mongo_collection (pymongo.collection.Collection):
            L'objet collection MongoDB dans lequel insérer le document.
        **kwargs:
            Les paires clé-valeur représentant les champs du document à insérer.

    Returns:
        ObjectId: L'identifiant (_id) du document inséré.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
