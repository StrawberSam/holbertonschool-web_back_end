#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retourne une page de données résiliente aux suppressions.

        La méthode parcourt l'indexation {index_original: ligne} en sautant
        les indices manquants (supprimés) pour collecter jusqu'à `page_size`
        éléments à partir de `index`. Elle renvoie aussi l'index à utiliser
        pour la requête suivante (next_index).

        Args:
            index (int | None): Index de départ (0 par défaut si None).
            page_size (int): Taille de page demandée.

        Returns:
            Dict: {
                'index': index de départ demandé,
                'data': liste des lignes collectées,
                'page_size': taille réelle renvoyée (len(data)),
                'next_index': index à requêter pour la page suivante
            }

        Raises:
            AssertionError: si `index` n'est pas dans une plage valide.
        """
        # Normaliser & valider l'index
        if index is None:
            index = 0

        # S'assure que l'index est dans la plage du dataset "original"
        total_items = len(self.dataset())
        assert isinstance(index, int) and 0 <= index < total_items

        # Récupérer la structure indexée (avec trous possibles)
        indexed = self.indexed_dataset()

        # Collecter jusqu'à `page_size` éléments en sautant les trous
        data = []
        cursor = index
        while len(data) < page_size and cursor < total_items:
            if cursor in indexed:          # clé présente → ligne existante
                data.append(indexed[cursor])
            cursor += 1                    # on avance (trous inclus)

        # Construire la réponse
        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': cursor,          # là où reprendre le scan
        }

