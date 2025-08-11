#!/usr/bin/env python3
"""
Module de pagination simple.

Ce module contient une fonction `index_range` qui calcule
les indices de début et de fin pour extraire une portion
d'une liste, selon les paramètres de pagination donnés.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calcule la plage d'indices pour une pagination donnée.

    Args:
        page (int): Numéro de la page (à partir de 1).
        page_size (int): Nombre d'éléments par page.

    Returns:
        tuple: Un tuple (start_index, end_index) où :
            - start_index est l'indice du premier élément de la page.
            - end_index est l'indice du premier élément de la page suivante.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
