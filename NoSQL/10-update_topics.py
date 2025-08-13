#!/usr/bin/env python3
"""
Module update_topics
Ce module fournit une fonction pour mettre à jour la liste des sujets
(topics) d'une école dans une collection MongoDB à partir de son nom,
en utilisant la bibliothèque PyMongo.
"""


def update_topics(mongo_collection, name, topics):
    """
    Met à jour les topics d'une école dans la collection MongoDB.

    Args:
        mongo_collection (pymongo.collection.Collection):
            L'objet collection MongoDB contenant les documents des écoles.
        name (str):
            Le nom de l'école à mettre à jour.
        topics (list[str]):
            La liste des sujets (topics) à associer à l'école.

    Returns:
        None
    """
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
)
