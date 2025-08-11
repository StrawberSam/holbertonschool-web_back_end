#!/usr/bin/env python3
"""
Module de pagination simple.

Ce module contient une fonction `index_range` qui calcule
les indices de début et de fin pour extraire une portion
d'une liste, selon les paramètres de pagination donnés.
"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retourne une page de données depuis le dataset.

        Cette méthode utilise la fonction `index_range` pour calculer les
        indices de début et de fin correspondant aux paramètres de pagination,
        puis retourne la sous-liste appropriée du dataset.

        Args:
            page (int) : Numéro de la page à récupérer (défaut : 1).
                                    Doit être un entier strictement positif.
           page_size (int) : Nombre d'éléments par page (défaut : 10).
                                     Doit être un entier strictement positif.

        Returns:
           List[List] : Liste des lignes correspondant à la page demandée.
                         Retourne une liste vide si `page` est hors plage.

        Raises:
            AssertionError: Si `page` ou `page_size` ne sont pas des entiers
                            strictement positifs.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]


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
