"""Esempio essenziale di CPM mediante un grafo aciclico delle attività."""

import networkx as nx


attivita = nx.DiGraph()
attivita.add_node("A", durata=3)
attivita.add_node("B", durata=2)
attivita.add_node("C", durata=4)
attivita.add_node("D", durata=2)
attivita.add_edges_from([("A", "C"), ("B", "C"), ("C", "D")])

inizio = {}
fine = {}
for nodo in nx.topological_sort(attivita):
    predecessori = list(attivita.predecessors(nodo))
    inizio[nodo] = max((fine[p] for p in predecessori), default=0)
    fine[nodo] = inizio[nodo] + attivita.nodes[nodo]["durata"]

print("Tempi al più presto:")
for nodo in attivita:
    print(f"{nodo}: inizio={inizio[nodo]}, fine={fine[nodo]}")
print(f"Durata del progetto: {max(fine.values())}")

