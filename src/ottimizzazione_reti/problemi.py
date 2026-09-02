"""Semplici involucri attorno agli algoritmi NetworkX usati nelle dispense."""

from __future__ import annotations

from collections.abc import Hashable

import networkx as nx


def verifica_domande(grafo: nx.DiGraph) -> None:
    """Verifica che le domande dei nodi siano bilanciate.

    La convenzione è quella di NetworkX: domanda positiva per un nodo che
    consuma e negativa per un nodo che offre flusso.
    """
    totale = sum(dati.get("demand", 0) for _, dati in grafo.nodes(data=True))
    if totale != 0:
        raise ValueError(f"Il problema non è bilanciato: somma domande = {totale}")


def flusso_costo_minimo(grafo: nx.DiGraph) -> tuple[int | float, dict]:
    """Restituisce costo ottimo e flusso di costo minimo."""
    verifica_domande(grafo)
    flusso = nx.min_cost_flow(grafo, demand="demand", capacity="capacity", weight="weight")
    costo = nx.cost_of_flow(grafo, flusso, weight="weight")
    return costo, flusso


def massimo_flusso(
    grafo: nx.DiGraph, sorgente: Hashable, pozzo: Hashable
) -> tuple[int | float, dict]:
    """Restituisce valore e dizionario di un flusso massimo."""
    return nx.maximum_flow(grafo, sorgente, pozzo, capacity="capacity")


def cammino_minimo(
    grafo: nx.Graph, origine: Hashable, destinazione: Hashable
) -> tuple[int | float, list[Hashable]]:
    """Restituisce lunghezza e nodi di un cammino minimo."""
    lunghezza = nx.shortest_path_length(grafo, origine, destinazione, weight="weight")
    cammino = nx.shortest_path(grafo, origine, destinazione, weight="weight")
    return lunghezza, cammino

