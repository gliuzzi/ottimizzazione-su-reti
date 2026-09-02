"""Esempio di flusso a costo minimo con la convenzione NetworkX."""

import networkx as nx

from ottimizzazione_reti import flusso_costo_minimo


rete = nx.DiGraph()
rete.add_node("s", demand=-5)  # offerta di 5 unità
rete.add_node("a", demand=0)
rete.add_node("b", demand=0)
rete.add_node("t", demand=5)   # domanda di 5 unità

rete.add_edge("s", "a", capacity=4, weight=2)
rete.add_edge("s", "b", capacity=3, weight=1)
rete.add_edge("a", "b", capacity=2, weight=1)
rete.add_edge("a", "t", capacity=4, weight=1)
rete.add_edge("b", "t", capacity=4, weight=3)

costo, flusso = flusso_costo_minimo(rete)
print(f"Costo ottimo: {costo}")
for i, uscenti in flusso.items():
    for j, valore in uscenti.items():
        if valore:
            print(f"x[{i},{j}] = {valore}")

