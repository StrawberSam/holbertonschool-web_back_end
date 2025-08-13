#!/usr/bin/env python3
"""
Module schools_by_topic
Ce module contient une fonction pour récupérer la liste des écoles
ayant un sujet spécifique dans leur champ 'topics'.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Retourne la liste des écoles ayant un sujet spécifique.

    Args:
        mongo_collection (pymongo.collection.Collection):
            L'objet collection MongoDB contenant les documents des écoles.
        topic (str):
            Le sujet à rechercher dans le champ 'topics'.

    Returns:
        list[dict]: Liste des documents correspondant au sujet recherché.
    """

    return list(mongo_collection.find({ "topics": topic }))
