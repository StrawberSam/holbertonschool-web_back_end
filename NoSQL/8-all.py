#!/usr/bin/env python3
"""
Module list_all
Ce module contient une fonction permettant de lister tous les documents d'une
collection MongoDB en utilisant PyMongo.
"""

from pymongo import MongoClient

def list_all(mongo_collection):
    """
    Liste tous les documents d'une collection MongoDB.

    Args:
        mongo_collection (pymongo.collection.Collection):
            L'objet collection MongoDB sur lequel exécuter la requête.

    Returns:
        list: Liste de tous les documents présents dans la collection.
              Retourne une liste vide si aucun document n'est trouvé.
    """
    return list(mongo_collection.find())
