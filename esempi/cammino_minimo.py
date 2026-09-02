"""Esempio di cammino minimo pesato."""

import networkx as nx

from ottimizzazione_reti import cammino_minimo


grafo = nx.DiGraph()
grafo.add_weighted_edges_from(
    [("s", "a", 4), ("s", "b", 2), ("b", "a", 1), ("a", "t", 3), ("b", "t", 7)]
)

lunghezza, cammino = cammino_minimo(grafo, "s", "t")
print(f"Cammino minimo: {' -> '.join(cammino)}")
print(f"Lunghezza: {lunghezza}")

