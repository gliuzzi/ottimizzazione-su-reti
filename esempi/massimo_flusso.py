"""Esempio di massimo flusso."""

import networkx as nx

from ottimizzazione_reti import massimo_flusso


rete = nx.DiGraph()
rete.add_edge("s", "a", capacity=7)
rete.add_edge("s", "b", capacity=4)
rete.add_edge("a", "b", capacity=3)
rete.add_edge("a", "t", capacity=5)
rete.add_edge("b", "t", capacity=6)

valore, flusso = massimo_flusso(rete, "s", "t")
print(f"Valore del flusso massimo: {valore}")
print(flusso)

